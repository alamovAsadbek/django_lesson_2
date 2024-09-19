from django.db import models

from groups.models import GroupsModel
from users.models import UsersModel


class GroupStudentModel(models.Model):
    group_id = models.ForeignKey(GroupsModel, on_delete=models.SET_NULL, null=True)
    student_id = models.ForeignKey(UsersModel, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Group Students'
        verbose_name = 'Group Student'
