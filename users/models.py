from typing import Any
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from typing import Optional


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(
        self,
        name: str,
        address: str,
        age: int,
        password=Optional[str],
        **kwargs,
    ):
        if not name:
            ValueError("이름은 필수 사항입니다.")
        user = self.model(
            name=name,
            address=address,
            age=age,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        name: str,
        address: str,
        age: int,
        password=Optional[str],
        **extra_fields,
    ):
        user = self.create_user(name=name, address=address, age=age, password=password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = [
        "age",
        "address",
    ]

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin
