from django.db import models


class UsersModel(models.Model):
    STATUS_CHOICES = (
        ('student', 'student'),
        ('teacher', 'teacher')
    )
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Phone Number')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='student', verbose_name='Status')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
