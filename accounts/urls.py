from django.urls import path
from .views import (ProfileAPIView, FriendCreateAPIView, FriendDeleteAPIView,
                    AllProfilesAPIView, CreateGroupAPIView, AddMemberAPIView,
                    GroupListAPIView,)

urlpatterns = [
    path('profile/', ProfileAPIView.as_view()),
    path('all-profile/', AllProfilesAPIView.as_view()),
    path('add-friend/', FriendCreateAPIView.as_view()),
    path('delete-friend/<int:pk>', FriendDeleteAPIView.as_view()),
    path('create-group/', CreateGroupAPIView.as_view()),
    path('add-member-in-group/', AddMemberAPIView.as_view()),
    path('groups/', GroupListAPIView.as_view())
]
