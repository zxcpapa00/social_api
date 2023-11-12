import uuid
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class UserAccountManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        return super().create_user(email, password=None, **extra_fields)


class User(AbstractUser):
    is_verified = models.BooleanField('verified', default=False)
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)

    objects = UserAccountManager()

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/', default='user_images/default/default-avatar-profile.jpg')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.friend} friend for {self.user}'


class Group(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return f'group: {self.name}'


class GroupMember(models.Model):
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE, related_name='members')
    member = models.ForeignKey(to=User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.member} member in {self.group}'
