from django.db import models


# Create your models here.
class Profile(models.Model):
    user_profile = models.OneToOneField("users.User", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
