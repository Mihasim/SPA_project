from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from study.models import Course, Lesson
import datetime

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


class UserSubscriptions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='subscribers')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    sign_of_subscription = models.BooleanField(default=True, verbose_name='признак подписки')

    subscriptions = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                                      verbose_name='подписки')

    def __str__(self):
        return f'{self.user},{self.course},{self.sign_of_subscription}'

    class Meta:
        verbose_name = 'пользовательская подписка'
        verbose_name_plural = 'пользовательские подписки'


class Payments(models.Model):
    METHOD_CASH = 'cash'
    METHOD_TRANSFER = 'transfer'

    PAYMENT_METHODS = [
        (METHOD_CASH, 'наличные'),
        (METHOD_TRANSFER, 'перевод'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_payments = models.DateField(default=datetime.datetime.now(), verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    payment_amount = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=50, verbose_name='способ оплаты', choices=PAYMENT_METHODS)

    def __str__(self):
        return f'{self.user}, {self.date_payments}, {self.payment_amount}, {self.payment_method}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
        ordering = ['-date_payments']
