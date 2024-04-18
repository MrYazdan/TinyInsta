from django.shortcuts import get_object_or_404
from rest_framework import generics, response
from apps.post import serializers
from apps.post.models import Like, Post, Comment


# from rest_framework import views, response
# class PostView(views.APIView):
#     def get(self, request):
#         # return response.Response([{'id': p.id, 'title': p.title} for p in Post.objects.all()])
#         return response.Response(PostSerializer(Post.objects.all(), many=True).data)
#
#     def post(self, request):
#         data = self.request.data
#         serializer = PostSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(serializer.data)
#
#         return response.Response(serializer.errors)


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post
    serializer_class = serializers.PostSerializer

    def get_object(self):
        return get_object_or_404(self.queryset, pk=self.kwargs.get("pk"))


class PostLikesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikesSerializer

    def post(self, request, *args, **kwargs):
        user = self.request.user
        post = get_object_or_404(Post, pk=kwargs.get("pk"))
        like, like_status = Like.objects.get_or_create(user=user, post=post)

        if not like_status:
            like.delete()

        return response.Response({"status": like_status})


class PostCommentsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs.get("pk"))


class PostCommentsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.custom
    serializer_class = serializers.CommentSerializer

    def get_object(self):
        return get_object_or_404(self.queryset, pk=self.kwargs.get("comment_id"))

    # TODO : NOT COMPLETED !!!
