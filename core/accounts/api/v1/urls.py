from django.urls import path, include
from . import views


urlpatterns = [
    # registration
    path("registration/", views.RegistrationApiView.as_view(), "registration")
    # change password
    # reset password
    # login token
    # login JWT
]
