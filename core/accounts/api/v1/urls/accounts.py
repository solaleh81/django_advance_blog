from django.urls import path, include
from .. import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

urlpatterns = [
    # registration
    path("registration/", views.RegistrationApiView.as_view(), name="registration"),
    path("test-email/", views.TestEmailSend.as_view(), name="test-email"),
    # activation
    # path("activation/confirm/", views.ActivationView.as_view(), name
    # resend Activathon
    # path("activation/resend/", views.ResendView.as_view(),
    # change password
    path(
        "change_password/",
        views.ChangePasswordApiView.as_view(),
        name="change_password",
    ),
    # reset password
    # login token
    path("token/login/", views.CustomObtainTokenView.as_view(), name="token-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    # login JWT
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
