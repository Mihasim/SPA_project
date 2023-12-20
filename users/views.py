from django.shortcuts import render
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from users.models import User, Payments, UserSubscriptions
from users.serializers import UserSerializer, PaymentsSerializer, UserSubscriptionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Контроллер для взаимодействия с пользователями (CRUD)
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

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


class UserSubscriptionCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания подписки
    """

    queryset = UserSubscriptions.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [AllowAny]

class UserSubscriptionListAPIView(generics.ListAPIView):
    """
    Контроллер для вывода подписок
    """
    queryset = UserSubscriptions.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [AllowAny]

class UserSubscriptionDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер удаления создания подписки
    """

    queryset = UserSubscriptions.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [AllowAny]