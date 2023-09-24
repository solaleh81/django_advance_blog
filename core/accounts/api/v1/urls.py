from django.urls import path, include
from . import views


app_name = "api-v1"

urlpatterns = [
    # registration
    path("registration/", views.RegistrationApiView.as_view(), "registration")
    # change password
    # reset password
    # login token
    # login JWT
]
