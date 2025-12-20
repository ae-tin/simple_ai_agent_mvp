from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings


def verify_google_id_token(token: str) -> dict:
    """
    Google id_token 검증
    실패 시 Exception 발생
    """
    idinfo = id_token.verify_oauth2_token(
        token,
        requests.Request(),
        settings.GOOGLE_CLIENT_ID,
    )

    if idinfo["iss"] not in ["accounts.google.com", "https://accounts.google.com"]:
        raise ValueError("Invalid issuer")

    return idinfo
