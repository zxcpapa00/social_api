from rest_framework import generics

from content.models import Post
from content.serializers import PostSerializer, PostCreateSerializer


class PostsAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(draft=False)
    serializer_class = PostSerializer


class PostAPICreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

