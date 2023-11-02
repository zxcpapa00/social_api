from django.contrib.auth.models import User
from django.db.models import Count, F
from rest_framework import generics, status, filters
from rest_framework.response import Response

from .models import Profile, Friend, Group, GroupMember
from .serializers import (ProfileSerializer, FriendSerializer, AllProfileSerializer,
                          GroupCreateSerializer, GroupMemberSerializer, GroupSerializer)


class ProfileAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        super().get_queryset()
        return self.queryset.filter(user=self.request.user).annotate(
            total_friends=Count(F('user__friends'))
        )


class AllProfilesAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = AllProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'user__first_name', 'user__last_name']


class FriendCreateAPIView(generics.CreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user_id = int(request.data.get('friend'))
        friend = Friend.objects.filter(user=request.user, friend=user_id).exists()
        if user_id != request.user.id and not friend:
            return super().create(request, *args, **kwargs)
        return Response({'detail': 'You are already friends'}, status=status.HTTP_400_BAD_REQUEST)


class FriendDeleteAPIView(generics.DestroyAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def destroy(self, request, *args, **kwargs):
        friend = self.get_object()
        if friend.user == request.user:
            Friend.objects.get(friend=friend.user, user=friend.friend).delete()
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)


class CreateGroupAPIView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        group_id = response.data.get('id')
        GroupMember.objects.create(group_id=group_id, member=request.user, is_admin=True)
        return response


class AddMemberAPIView(generics.CreateAPIView):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer

    def create(self, request, *args, **kwargs):
        member = request.data.get('member')
        group = Group.objects.filter(id=int(request.data.get('group')))
        admin = group.first().members.filter(is_admin=True).first().member
        in_group = group.first().members.filter(member_id=member)

        if not in_group:
            if admin == request.user:
                return super().create(request, *args, **kwargs)
            return Response({'detail': 'You are not a admin'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'He is already in group'}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return self.queryset.filter(member=self.request.user)


class GroupMemberDeleteAPIView(generics.DestroyAPIView):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer


class GroupListAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        return self.queryset.filter(members__member__in=[self.request.user])
