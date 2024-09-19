from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    STATUS_CHOICES = (
        ('student', 'student'),
        ('teacher', 'teacher')
    )
    phone_number = models.IntegerField(unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='student')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
