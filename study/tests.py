from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from study.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

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

    def test_lesson_view(self):
        """
        Тестирование вывода уроков
        """
        response = self.client.get(
            '/lesson/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': self.lesson.id, 'name': self.lesson.name,
                 'description': self.lesson.description,
                 'preview': None, 'link_on_video': self.lesson.link_on_video,
                 'course_lesson': self.lesson.course_lesson.id, 'owner': self.lesson.owner.id}]}
        )

    def test_create_lesson(self):
        """
        Тестирование создания уроков
        """
        data = {
            'name': 'Test',
            'course_lesson': self.course.id
        }
        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 3, 'name': 'Test',
             'description': None, 'preview': None,
             'link_on_video': None,
             'course_lesson': self.course.id,
             'owner': self.lesson.owner.id}
        )


class UpdateLessonTest(APITestCase):
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
        self.data = (
            {'name': 'Test111',
            'course_lesson': self.course.id}
        )

    def test_update_lesson(self):
        """
        Тестирование изменения уроков
        """
        response = self.client.put(
            f'/lesson/update/{self.lesson.id}/',
            data=self.data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': self.lesson.id,
             'name': 'Test111',
             'description': self.lesson.description,
             'preview': None,
             'link_on_video': None,
             'course_lesson': self.lesson.course_lesson.id,
             'owner': self.lesson.owner.id}
        )

class ViewOneLessonTest(APITestCase):
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
        self.data = (
            {'name': 'Test111',
             'course_lesson': self.course.id}
        )

    def test_one_lesson_view(self):
        """
        Тестирование вывода одного урока
        """

        response = self.client.get(
            f'/lesson/{self.lesson.id}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': self.lesson.id,
             'name': self.lesson.name,
             'description': self.lesson.description,
             'preview': None,
             'link_on_video': None,
             'course_lesson': self.lesson.course_lesson.id,
             'owner': self.lesson.owner.id}
        )


class DeleteLessonTest(APITestCase):
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
        self.data = (
            {'name': 'Test111',
             'course_lesson': self.course.id}
        )

    def test_lesson_delete(self):
        """
        Тестирование удаления урока
        """
        response = self.client.delete(
            f'/lesson/delete/{self.lesson.id}/',
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Lesson.objects.count(), 0
        )
