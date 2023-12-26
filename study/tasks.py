from datetime import datetime, timedelta

from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.mail import send_mail
import pytz

from users.models import User


@shared_task
def update_course(users, course):
    send_mail(
        subject='Обновление материалов курса',
        message=f'В курсе "{course}", произошли какие-то бновления',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=users,
        fail_silently=False
    )


@shared_task
def check_user_last_login():
    current_time = pytz.utc.localize(datetime.now())
    for user in User.objects.all():
        if user.last_login is not None:
            if user.last_login <= current_time - timedelta(days=120):
                user.is_active = False
                user.save()
