from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly, AllowAny

from study.models import Course, Lesson
from study.paginators import CoursePaginator, lessonPaginator
from study.permissions import IsOwnerOrStaff, IsOwner, CoursePermission, IsModerator
from study.serializers import CourseSerializer, LessonSerializer


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
    permission_classes = [CoursePermission]
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        purchased_course = serializer.save()
        purchased_course.user = self.request.user
        purchased_course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания уроков
    """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        purchased_lesson = serializer.save()
        purchased_lesson.owner = self.request.user
        purchased_lesson.save()


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


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер для удаления урока
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]



