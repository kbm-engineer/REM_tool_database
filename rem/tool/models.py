from django.db import models
from smart_selects.db_fields import ChainedForeignKey

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
    name = models.CharField(max_length=100, unique=True)
    type = models.ForeignKey(TypeEquipment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
