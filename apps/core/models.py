from django.db import models
from apps.core.managers import LogicalManager


class TimeStampMixin(models.Model):
    """
    TimeStamp model mixin:

    fields:
        - create_at: DateTimeField (auto implement)
        - modify_at: DateTimeField (auto implement)
    """

    create_at = models.DateTimeField(auto_now_add=True, editable=False)
    modify_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class LogicalMixin(models.Model):
    """
    Logical model mixin:

    fields:
        - is_active: BooleanField (default True)
        - is_deleted: BooleanField (default False)
    """

    objects = LogicalManager()

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
