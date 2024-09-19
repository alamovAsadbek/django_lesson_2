from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    phone_number = models.IntegerField(unique=True)
