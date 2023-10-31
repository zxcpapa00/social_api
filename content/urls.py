from django.urls import path
from .views import (PostsAPIView, PostAPICreateView,
                    PostDetailAPIView, PostRefactorAPIView,
                    LikeAPIView, CommentCreateAPIView)

urlpatterns = [
    path('posts/', PostsAPIView.as_view()),
    path('posts/<int:pk>', PostDetailAPIView.as_view()),
    path('posts/update/<int:pk>', PostRefactorAPIView.as_view()),
    path('create-post/', PostAPICreateView.as_view()),
    path('create-comment/', CommentCreateAPIView.as_view()),
    path('create-like/', LikeAPIView.as_view({'post': 'create'})),
    path('delete-like/<int:pk>', LikeAPIView.as_view({'delete': 'destroy'})),
]
