from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Profile, Group, GroupMember, Friend


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(signal=post_save, sender=Friend)
def create_friend(sender, instance, created, **kwargs):
    friend = Friend.objects.filter(user=instance.friend, friend=instance.user).exists()
    if created and not friend:
        Friend.objects.create(user=instance.friend, friend=instance.user)
