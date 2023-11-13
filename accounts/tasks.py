from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse

from social_api.celery import app


@app.task
def send_verification_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            'Verify your  account',
            'Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
            'zxcpapa00@gmail.com',
            [user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        print("Tried to send verification email to non-existing user '%s'" % user_id)


@app.task
def send_friend_notification(user_id, friend_id):
    UserModel = get_user_model()

    user = UserModel.objects.get(pk=user_id)
    friend = UserModel.objects.get(pk=friend_id)
    send_mail(
        'New friend',
        f'{friend} send you application',
        'zxcpapa00@gmail.com',
        [user.email],
        fail_silently=False,
    )


@app.task
def send_group_notification(user_id, admin_id, group_name):
    UserModel = get_user_model()

    user = UserModel.objects.get(pk=user_id)
    admin = UserModel.objects.get(pk=admin_id)

    send_mail(
        'Add in group',
        f'{admin} add you in group: {group_name}',
        'zxcpapa00@gmail.com',
        [user.email],
        fail_silently=False,
    )
