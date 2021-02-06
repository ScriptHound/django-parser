from django.db import models
from django.db.models.base import Model


# Create your models here.
class ResultIdModel(models.Model):
    pid = models.CharField(max_length=200)


class ResultRow(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    parent_id = models.ForeignKey(ResultIdModel, on_delete=models.CASCADE)
