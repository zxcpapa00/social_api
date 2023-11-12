from .models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, Friend
from .tasks import send_verification_email, send_friend_notification


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(signal=post_save, sender=Friend)
def create_friend(sender, instance, created, **kwargs):
    friend = Friend.objects.filter(user=instance.friend, friend=instance.user).exists()
    if created and not friend:
        send_friend_notification.delay(instance.friend.id, instance.user.id)
        Friend.objects.create(user=instance.friend, friend=instance.user)


@receiver(signal=post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if not instance.is_verified:
        send_verification_email.delay(instance.pk)
