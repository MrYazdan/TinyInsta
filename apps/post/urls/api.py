from django.urls import path

from apps.post.views import api

urlpatterns = [path("", api.PostView.as_view())]
