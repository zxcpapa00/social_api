from django.urls import path
from .views import ProfileAPIView, FriendCreateAPIView, FriendDeleteAPIView

urlpatterns = [
    path('profile/', ProfileAPIView.as_view()),
    path('add-friend/', FriendCreateAPIView.as_view()),
    path('delete-friend/<int:pk>', FriendDeleteAPIView.as_view()),
]
