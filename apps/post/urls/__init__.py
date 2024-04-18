from django.urls import path, include

urlpatterns = [
    path("posts/", include("apps.post.urls.post")),
    path("api/posts", include("apps.post.urls.api")),
]
