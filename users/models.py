from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    STATUS_CHOICES = (
        ('student', 'student'),
        ('teacher', 'teacher')
    )
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Phone Number')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='student', verbose_name='Status')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
