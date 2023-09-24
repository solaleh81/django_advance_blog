from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls

app_name = "api-v1"

urlpatterns = [
    # path("post/", views.postlist, name="post-list"),
    # path("post/<id>/", views.postDetail, name="post-detail"),
    # path("post/", views.PostList.as_view(), name="post-list"),
    # path("post/<pk>/", views.PostDetail.as_view(), name="post-detail"),
    path(
        "post/",
        views.PostModelViewSet.as_view({"get": "list", "post": "create"}),
        name="post-list",
    ),
    path(
        "post/<int:pk>/",
        views.PostModelViewSet.as_view({"get": "retrieve", "put": "update"}),
        name="post-retrieve",
    ),
]
