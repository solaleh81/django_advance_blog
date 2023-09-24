from django.urls import path, include


app_name = "accounts"

urlpatterns = [
    path("api/v1/", include("blog.api.v1.urls")),
]