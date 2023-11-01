from rest_framework import serializers

from .models import Profile, Friend, Group, GroupMember


class FriendSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(source='friend.username', read_only=True)
    first_name = serializers.CharField(source='friend.first_name', read_only=True)
    last_name = serializers.CharField(source='friend.last_name', read_only=True)

    class Meta:
        model = Friend
        fields = ['id', 'username', 'first_name', 'last_name', 'friend']


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    total_friends = serializers.IntegerField()
    friends = FriendSerializer(many=True, read_only=True, source='user.my_friends')

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email',
                  'image', 'description', 'total_friends', 'friends']


class AllProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'first_name', 'last_name', 'image', 'description']


class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = '__all__'


class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    members = GroupMemberSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'
