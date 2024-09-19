from django.db import models


class Lessons(models.Model):
    name = models.CharField(max_length=100)
    group_id = models.ForeignKey(GroupModal)
