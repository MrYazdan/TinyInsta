from django.urls import path, include

urlpatterns = [
    path("post/", include("apps.post.urls.post")),
]
