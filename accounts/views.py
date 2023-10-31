from django.db.models import Count, F
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Profile, Friend
from .serializers import ProfileSerializer, FriendSerializer


class ProfileAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        super().get_queryset()
        return self.queryset.filter(user=self.request.user).annotate(
            all_friends=Count(F('user__my_friends'))
        )


class FriendCreateAPIView(generics.CreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendDeleteAPIView(generics.DestroyAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def destroy(self, request, *args, **kwargs):
        friend = self.get_object()
        if friend.user == request.user:
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)
