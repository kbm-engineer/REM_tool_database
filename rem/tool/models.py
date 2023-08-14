from typing import Iterable, Optional
from django.db import models
import random


class BaseMonitoringObject(models.Model):
    id_number = models.IntegerField(unique=True, editable=False)
    name = models.CharField(max_length=100, unique=True)


    def save(self, *args, **kwargs) -> None:
        if not self.id_number:
            self.id_number = random.randint(1000, 9999)  # Генерация случайного числа
        super(BaseMonitoringObject, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
