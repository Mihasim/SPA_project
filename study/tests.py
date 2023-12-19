from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from study.models import Course, Lesson
from users.models import User


class lessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            name='Test course',
            description='Test Course description',
            owner=self.user, )
        self.lesson = Lesson.objects.create(
            name='Test lesson',
            description='Test lesson description',
            course_lesson=self.course,
            owner=self.user,
        )

    def test_lesson_view(self):
        """
        Тестирование вывода уроков
        """
        response = self.client.get(
            '/lesson/'
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)

    def test_create_lesson(self):
        """
        Тестирование создания уроков
        """
        data = {
            'name': 'Test',
            'course_lesson': 1
        }
        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_lesson(self):
        """
        Тестирование изменения уроков
        """

        data = {
            'name': 'Test111',
            'course_lesson': 1
        }
        response = self.client.post(
            '/lesson/update/2/',
            data=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 2,
             'name': 'Test111',
             'description': None,
             'preview': None,
             'link_on_video': None,
             'course_lesson': 1,
             'owner': 1}
        )

    def test_one_lesson_view(self):
        """
        Тестирование вывода одного урока
        """

        response = self.client.get(
            '/lesson/1/'
        )

        print("один", response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'name': 'Test lesson', 'description': 'Test lesson description', 'preview': None,
             'link_on_video': None, 'course_lesson': 1, 'owner': 1}
        )

    def test_lesson_delete(self):
        """
        Тестирование удаления урока
        """

        response = self.client.get(
            '/lesson/delete/1/'
        )

        print("один", response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Lesson.objects.count(), 0
        )


