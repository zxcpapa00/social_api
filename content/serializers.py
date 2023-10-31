from rest_framework import serializers

from content.models import Post, Like, Comment


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    likes_count = serializers.IntegerField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'image', 'author', 'date_create', 'likes_count']


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ['author']


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['id', 'post']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'body', 'post']
