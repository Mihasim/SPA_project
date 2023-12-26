from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly, AllowAny

from study.models import Course, Lesson
from study.paginators import CoursePaginator, lessonPaginator
from study.permissions import IsOwnerOrStaff, IsOwner, CoursePermission, IsModerator
from study.serializers import CourseSerializer, LessonSerializer
from study.tasks import update_course
from users.models import UserSubscriptions
from users.services import create_good


class REadOnly(BasePermission):
    """
    Разрешает просмотр
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class CourseViewSet(viewsets.ModelViewSet):
    """
    Контроллер для взаимодействия с курсами (CRUD)
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        purchased_course = serializer.save()
        purchased_course.owner = self.request.user
        purchased_course.course_id = create_good(purchased_course.name, purchased_course.description, purchased_course.price)  # Создаем товар и получаем его id
        purchased_course.save()

    def perform_update(self, serializer):
        purchased_course = serializer.save()

        subscribers = UserSubscriptions.objects.filter(course_id=purchased_course.id)
        if subscribers.exists():
            subscriber_list = []
            for subscriber in subscribers:
                subscriber_list.append(subscriber.user.email)
            update_course.delay(subscriber_list, purchased_course.name)
            print(f'обновлен курс {purchased_course.name}, на него подписаны: {", ".join(subscriber_list)}.')


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания уроков
    """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        purchased_lesson = serializer.save()
        purchased_lesson.owner = self.request.user
        purchased_lesson.lesson_id = create_good(purchased_lesson.name, purchased_lesson.description, purchased_lesson.price)  # Создаем товар и получаем его id
        purchased_lesson.save()

        subscribers = UserSubscriptions.objects.filter(course_id=purchased_lesson.course_lesson.id)
        if subscribers.exists():
            subscriber_list = []
            for subscriber in subscribers:
                subscriber_list.append(subscriber.user.email)
            update_course.delay(subscriber_list, purchased_lesson.course_lesson.name)
            print(f'Для курса {purchased_lesson.course_lesson.name} добавлен урок {purchased_lesson.name} на него подписаны: {", ".join(subscriber_list)}.')





class LessonListAPIView(generics.ListAPIView):
    """
    Контроллер для вывода списка уроков
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    pagination_class = lessonPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер для вывода одного урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер для редактирования урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]

    def perform_update(self, serializer):
        purchased_lesson = serializer.save()

        subscribers = UserSubscriptions.objects.filter(course_id=purchased_lesson.course_lesson.id)
        if subscribers.exists():
            subscriber_list = []
            for subscriber in subscribers:
                subscriber_list.append(subscriber.user.email)
            update_course(purchased_lesson.course_lesson.name, subscriber_list)
        print(f'Для курса {purchased_lesson.course_lesson.name} обновлен урок {purchased_lesson.name} на него подписаны: {", ".join(subscriber_list)}.')


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер для удаления урока
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]



