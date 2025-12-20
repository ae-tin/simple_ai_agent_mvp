from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # OAuth (브라우저 리다이렉트)
    path("accounts/", include("accounts.urls")),
    # DRF API
    # path("api/", include("api.urls")),
]
