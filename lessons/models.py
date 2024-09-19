from django.db import models

from groups.models import GroupModel
from users.models import UserModel


class Lessons(models.Model):
    name = models.CharField(max_length=100)
    group_id = models.ForeignKey(GroupModel, on_delete=models.SET_NULL, null=True)
    teacher_id = models.OneToOneField(UserModel, on_delete=models.SET_NULL, null=True)
