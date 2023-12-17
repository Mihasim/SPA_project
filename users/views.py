from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Контроллер для взаимодействия с пользователями (CRUD)
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
