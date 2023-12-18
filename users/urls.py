from django.urls import path

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import UserViewSet, PaymentsListAPIView, UserSubscriptionCreateAPIView, UserSubscriptionDestroyAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    # rest_framework_simplejwt для получения и обновления токенов
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # payments
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),

    # UserSubscription
    path('subscription/create/', UserSubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/delete/<int:pk>/', UserSubscriptionDestroyAPIView.as_view(), name='subscription_delete'),
] + router.urls
