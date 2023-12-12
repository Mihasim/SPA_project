from django.core.management import BaseCommand

from study.models import Payments
from users.models import User


class Command(BaseCommand):
    """
    Добавление пользователей (пример)
    """
    def handle(self, *args, **options):
        users_list = [
            {'email': '1@mail.com', 'phone': '123344566', 'city': '1', 'is_active': True},
            {'email': '2@mail.com', 'phone': '123344566', 'city': '2', 'is_active': True},
            {'email': '3@mail.com', 'phone': '123344566', 'city': '3', 'is_active': True},
        ]

        users_for_create = []
        for user in users_list:
            users_for_create.append(
                User(**user)
            )

        User.objects.bulk_create(users_for_create)
