from django.urls import path, include

urlpatterns = [
    path("posts/", include("apps.post.urls.post")),
]
