from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=512)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
    image = models.ImageField(upload_to='posts_images/', blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.user} liked {self.post}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f'{self.user} comment {self.post} - {self.body}'




