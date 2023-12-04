from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "last_login",
            "is_superuser",
            "is_admin",
            "is_active",
            "groups",
            "user_permissions",
        )
