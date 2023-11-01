from django.db.models import F, Count
from django_filters import rest_framework
from rest_framework import generics, status, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from content.models import Post, Like, Comment
from content.serializers import (PostListSerializer, PostCreateSerializer,
                                 PostDetailSerializer, LikeSerializer,
                                 CommentSerializer)


class PostsAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(draft=False)
    serializer_class = PostListSerializer
    filter_backends = [filters.OrderingFilter, rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author']
    ordering_fields = ['date_create']
    search_fields = ['title', 'body', 'author__username']

    def get_queryset(self):
        queryset = self.queryset
        return queryset.annotate(
            likes_count=Count(F('likes')))


class PostAPICreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostRefactorAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def update(self, request, *args, **kwargs):
        if self.get_object().author == request.user:
            return super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        if self.get_object().author == request.user:
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LikeAPIView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        like = self.get_object()
        if like.user == request.user:
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
