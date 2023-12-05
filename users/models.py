from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    city = models.CharField(max_length=150, verbose_name='Город')
    avatar = models.ImageField(upload_to='user_avatar/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return (f'{self.email}: {self.phone}')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
