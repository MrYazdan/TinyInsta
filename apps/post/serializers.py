from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.post.models import Post, Like, Comment


User = get_user_model()


class CommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "image")
        read_only_fields = ("username", "image")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        # exclude = ('is_deleted',)
        # depth = 0


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ("create_at", "post", "id")
        read_only_fields = ("user",)


class CommentSerializer(serializers.ModelSerializer):
    user = CommentUserSerializer(read_only=True)
    replies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        exclude = ("modify_at", "post", "is_deleted", "is_active")
        read_only_fields = ("user",)
        extra_kwargs = {"replies": {"read_only": True}, "reply": {"write_only": True}}

    def get_fields(self):
        fields = super(self.__class__, self).get_fields()
        fields["replies"] = self.__class__(many=True)
        return fields
