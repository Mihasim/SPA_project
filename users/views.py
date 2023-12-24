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


class PaymentsViewSet(viewsets.ModelViewSet):
    """
    Контроллер для списка платежей (CRUD)
    """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        purchased_payment = serializer.save()
        purchased_payment.user = self.request.user
        purchased_payment.save()


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