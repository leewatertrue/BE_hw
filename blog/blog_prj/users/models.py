from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email=models.CharField(max_length=30, unique=True, null=False, blank=False)
    nickname=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.username
