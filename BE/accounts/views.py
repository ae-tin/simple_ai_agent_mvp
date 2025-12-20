import requests
from django.shortcuts import redirect
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import SocialAccount

User = get_user_model()


def google_login(request):
    google_auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        "?response_type=code"
        f"&client_id={settings.GOOGLE_CLIENT_ID}"
        f"&redirect_uri={settings.GOOGLE_REDIRECT_URI}"
        "&scope=openid%20email%20profile"
    )
    return redirect(google_auth_url)


def google_callback(request):
    code = request.GET.get("code")

    # 1. Google token 요청
    token_res = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        },
    ).json()

    access_token = token_res.get("access_token")

    # 2. 사용자 정보 요청
    user_info = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"},
    ).json()

    email = user_info["email"]
    name = user_info.get("name", "")

    google_user_id = user_info["id"]

    social = (
        SocialAccount.objects.filter(
            provider="google",
            provider_user_id=google_user_id,
        )
        .select_related("user")
        .first()
    )

    if social:
        user = social.user
    else:
        user, _ = User.objects.get_or_create(
            email=email,
            defaults={"name": name},
        )

        social = SocialAccount.objects.create(
            user=user,
            provider="google",
            provider_user_id=google_user_id,
            extra_data=user_info,
        )

    # 4. JWT 발급
    refresh = RefreshToken.for_user(user)

    # 5. Vue로 리다이렉트
    return redirect(f"http://localhost:5173/" f"?access={str(refresh.access_token)}" f"&refresh={str(refresh)}")
