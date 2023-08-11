from typing import Iterable, Optional
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
import time

class UniqueIdentificator(models.Model):
    nomber = models.TextField(max_length=16, unique=True, blank=True)

    def fill_nomber(self, instance, **kwargs):
        instance.nomber = str(time.time())


class ViewEquipment(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class TypeEquipment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    view = models.OneToOneField(ViewEquipment, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BaseMonitoringObject(models.Model):
    # id_nomber = 
    name = models.CharField(max_length=100, unique=True)
    type = models.ForeignKey(TypeEquipment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
