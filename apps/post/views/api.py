from rest_framework import views, response
from apps.post.models import Post
from apps.post.serializers import PostSerializer


class PostView(views.APIView):
    def get(self, request):
        # return response.Response([{'id': p.id, 'title': p.title} for p in Post.objects.all()])
        return response.Response(PostSerializer(Post.objects.all(), many=True).data)

    def post(self, request):
        data = self.request.data
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)

        return response.Response(serializer.errors)
