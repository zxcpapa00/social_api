from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/', default='user_images/default/default-avatar-profile.jpg')
    description = models.TextField()

    def __str__(self):
        return self.user.username





