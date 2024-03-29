from django.db import models
from apps.core.models import TimeStampMixin, LogicalMixin


class Post(TimeStampMixin, LogicalMixin):
    title = models.CharField(max_length=125)
    content = models.TextField()
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    tags = ...
    images = ...
