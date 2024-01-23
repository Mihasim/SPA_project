import random

from django.core.management import BaseCommand

from study.models import Course, Lesson
from users.models import User, Payments


class Command(BaseCommand):
    """
    Добавление оплаты (пример)
    """
    def handle(self, *args, **options):
        users = User.objects.all()
        courses = Course.objects.all()
        lessons = Lesson.objects.all()
        payment_method = ['cash', 'transfer']
        payment_list = []
        for user in users:
            for course in courses:
                for lesson in lessons:
                    payment_list.append(
                    {'user': user, 'paid_course': course, 'paid_lesson': lesson, 'payment_amount': 1000, 'payment_method': random.choice(payment_method)}
                    )


        payments_for_create = []
        for payment in payment_list:
            payments_for_create.append(
                Payments(**payment)
            )

        Payments.objects.bulk_create(payments_for_create)
