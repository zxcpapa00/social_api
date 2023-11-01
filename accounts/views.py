from django.db.models import Count, F
from rest_framework import generics, status, filters, viewsets
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
            total_friends=Count(F('user__my_friends'))
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
        if int(request.data.get('friend')) != request.user.id:
            return super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class FriendDeleteAPIView(generics.DestroyAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def destroy(self, request, *args, **kwargs):
        friend = self.get_object()
        if friend.user == request.user:
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
        print(request.data.get('group'))
        return super().create(request, *args, **kwargs)


class GroupListAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        return self.queryset.filter(members__member__in=[self.request.user])
