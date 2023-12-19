from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """
    Добавление пользователей (пример)
    """
    def handle(self, *args, **options):
        user = User.objects.create(
            email='123@mail.com',
            phone='123344123',
            city='1',
            is_staff=True,
            is_active=True
        )
        user.set_password('5482')
        user.save()

        user = User.objects.create(
            email='456@mail.com',
            phone='123344456',
            city='2',
            is_staff=True,
            is_active=True
        )
        user.set_password('5482')
        user.save()

        user = User.objects.create(
            email='789@mail.com',
            phone='123344789',
            city='3',
            is_active=True
        )
        user.set_password('5482')
        user.save()

