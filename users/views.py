from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import get_user_model
from . import serializers

User = get_user_model()


class UserViewSet(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
