from django.db import models

from groups.models import GroupsModel
from users.models import UsersModel


class LessonsModel(models.Model):
    name = models.CharField(max_length=100)
    group_id = models.ForeignKey(GroupsModel, on_delete=models.SET_NULL, null=True)
    teacher_id = models.OneToOneField(UsersModel, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Lessons'
        verbose_name = 'Lesson'
