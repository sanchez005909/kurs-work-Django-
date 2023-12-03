import uuid
from newsletter.models import NULLABLE
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    avatar = models.ImageField(verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=30, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=30, verbose_name='страна', **NULLABLE)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

