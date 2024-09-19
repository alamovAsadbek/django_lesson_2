from django.db import models

from groups.models import GroupModel


class GroupStudentModel(models.Model):
    group_id = models.ForeignKey(GroupModel, on_delete=models.SET_NULL, null=True)
