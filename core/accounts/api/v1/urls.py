from django.urls import path, include
from . import views

urlpatterns = [
    # registration
    path("registration/", views.RegistrationApiView.as_view(), name="registration"),
    path("token/login/", views.CustomObtainTokenView.as_view(), name="token-login")
    # change password
    # reset password
    # login token
    # login JWT
]
