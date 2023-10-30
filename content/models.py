from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=512)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
    image = models.ImageField(upload_to='posts_images/')
    date_create = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField(default=False)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()




