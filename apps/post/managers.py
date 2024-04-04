from apps.core.managers import LogicalManager


class CommentManager(LogicalManager):
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset().filter(reply__isnull=True)
