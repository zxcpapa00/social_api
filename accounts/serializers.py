from rest_framework import serializers

from .models import Profile, Friend


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    all_friends = serializers.IntegerField()
    friends = FriendSerializer(many=True, read_only=True, source='user.my_friends')

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email',
                  'image', 'description', 'all_friends', 'friends']
