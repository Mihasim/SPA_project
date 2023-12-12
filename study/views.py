from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from study.models import Course, Lesson, Payments
from study.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    Контроллер для взаимодействия с курсами (CRUD)
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер для вывода курса вместе с уроками
    """
    serializer_class = CourseSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания уроков
    """
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """
    Контроллер для вывода списка уроков
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер для вывода урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер для редактирования урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер для удаления урока
    """
    queryset = Lesson.objects.all()


class PaymentsListAPIView(generics.ListAPIView):
    """
    Контроллер для вывода списка платежей
    """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')  # фильтровать можно по этим полям
    ordering_fields = ('date_payments',)  # сортировка по дате оплаты
