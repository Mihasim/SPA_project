import requests
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


    def get_payment_link(self):
        url = 'https://api.stripe.com/v1/checkout/sessions'
        response = requests.request('GET', url)


class UserSubscriptionSerializer(serializers.ModelSerializer):
    """
    Сереализатор подписок
    """
    class Meta:
        model = UserSubscriptions
        fields = '__all__'

