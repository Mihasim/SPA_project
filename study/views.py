from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly

from study.models import Course, Lesson, Payments
from study.permissions import IsOwnerOrStaff, IsOwner, CoursePermission
from study.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer


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

    def perform_create(self, serializer):
        purchased_course = serializer.save()
        purchased_course.owner = self.request.user
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
    permission_classes = [IsOwnerOrStaff]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер для вывода урока
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


class PaymentsListAPIView(generics.ListAPIView):
    """
    Контроллер для вывода списка платежей
    """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')  # фильтровать можно по этим полям
    ordering_fields = ('date_payments',)  # сортировка по дате оплаты
    permission_classes = [IsAuthenticated]
