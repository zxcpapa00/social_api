from rest_framework import serializers

from content.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField()

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ['author']

