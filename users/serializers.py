import requests
import stripe
from rest_framework import serializers

from users.models import User, Payments, UserSubscriptions


class UserSerializer(serializers.ModelSerializer):
    """
    Сереализатор для пользователя
    """
    class Meta:
        model = User
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):
    """
    Сереализатор для платежей
    """
    class Meta:
        model = Payments
        fields = '__all__'



class UserSubscriptionSerializer(serializers.ModelSerializer):
    """
    Сереализатор подписок
    """
    class Meta:
        model = UserSubscriptions
        fields = '__all__'

