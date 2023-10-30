from rest_framework import generics

from .models import Profile
from .serializers import ProfileSerializer


class ProfileAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        super().get_queryset()
        return self.queryset.filter(user=self.request.user)
