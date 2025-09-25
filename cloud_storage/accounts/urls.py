from django.urls import path
from .views import (
    RegisterView,
    LogoutView,
    AuthTokenView,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path("auth/sign-up/", RegisterView.as_view(), name="register"),
    path("auth/sign-in/", AuthTokenView.as_view(), name="token_obtain_pair"),
    path("auth/sign-out/", LogoutView.as_view(), name="logout"),
    path("token/refresh/",  TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
