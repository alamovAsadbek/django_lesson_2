from django.db import models

from groups.models import GroupsModel


class GroupStudentModel(models.Model):
    group_id = models.ForeignKey(GroupsModel, on_delete=models.SET_NULL, null=True)
