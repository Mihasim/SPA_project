from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from study.models import Course, Lesson
from users.models import User, UserSubscriptions


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            name='Test course',
            description='Test Course description',
            owner=self.user,
        )
        self.lesson = Lesson.objects.create(
            name='Test lesson',
            description='Test lesson description',
            course_lesson=self.course,
            owner=self.user,
        )
        self.subscriptions = UserSubscriptions.objects.create(
            user=self.user,
            course=self.course,
        )

    def test_subscriptions_view(self):
        """
        Тестирование вывода подписок
        """
        response = self.client.get(
            '/users/subscription/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)


class SubscriptionCreateTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            name='Test course',
            description='Test Course description',
            owner=self.user,
        )
        self.lesson = Lesson.objects.create(
            name='Test lesson',
            description='Test lesson description',
            course_lesson=self.course,
            owner=self.user,
        )

    def test_create_subscriptions(self):
        """
        Тестирование создания подписки
        """
        data = {
            'user': self.user.id,
            'course': self.course.id
        }
        response = self.client.post(
            '/users/subscription/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


class SubscriptionDeleteTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            name='Test course',
            description='Test Course description',
            owner=self.user,
        )
        self.lesson = Lesson.objects.create(
            name='Test lesson',
            description='Test lesson description',
            course_lesson=self.course,
            owner=self.user,
        )
        self.subscriptions = UserSubscriptions.objects.create(
            user=self.user,
            course=self.course,
        )
    def test_delete_subscriptions(self):
        """
        Тестирование удаления подписки
        """
        response = self.client.delete(
            f'/users/subscription/delete/{self.subscriptions.id}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            UserSubscriptions.objects.count(), 0
        )
