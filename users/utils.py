from random import choice

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse


def generate_new_password(request):
    new_password = make_random_password()
    send_mail(
        subject='Сгенерирован новый пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:profile'))


def make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'):
    return ''.join([choice(allowed_chars) for i in range(length)])