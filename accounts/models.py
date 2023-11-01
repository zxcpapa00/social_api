from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/', default='user_images/default/default-avatar-profile.jpg')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_friends')
    friend = models.OneToOneField(User, on_delete=models.CASCADE, related_name='friends')

    def __str__(self):
        return f'{self.friend} friend for {self.user}'


class Group(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return f'group: {self.name}'


class GroupMember(models.Model):
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE, related_name='members')
    member = models.OneToOneField(to=User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.member} member in {self.group}'
