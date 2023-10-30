from django.urls import path
from .views import PostsAPIView, PostAPICreateView

urlpatterns = [
    path('posts/', PostsAPIView.as_view()),
    path('create-post/', PostAPICreateView.as_view()),
]
