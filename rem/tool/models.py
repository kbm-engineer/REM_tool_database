from django.db import models
import time, datetime
from datetime import timedelta


# class BaseMonitoringObject(models.Model):
#     id_number = models.IntegerField(unique=True, editable=False, verbose_name = "Уникальный номер")
#     name = models.CharField(max_length=100, unique=True, verbose_name = "Наименование")
#     create_date = models.DateField(editable=False, verbose_name = "Дата производства")
#     update_date = models.DateField(editable=False, blank=True, null=True, verbose_name = "Дата редактирования")
#     start_date_use = models.DateField(blank=True, null=True, verbose_name = "Дата начала эксплуатации")
#     end_warranty = models.DateField(blank=True, null=True, verbose_name = "Дата окончания гарантии")

#     def save(self, *args, **kwargs) -> None:
#         if not self.id_number:
#             self.id_number = time.time()
#             self.create_date = datetime.datetime.today()
#         else:
#             self.update_date = datetime.datetime.today()
#         if self.start_date_use is not None and not self.end_warranty:
#             self.end_warranty = self.start_date_use + timedelta(days=365)
#         super(BaseMonitoringObject, self).save(*args, **kwargs)
    
#     @property
#     def number_days_warranty(self):
#         if self.start_date_use:
#             if self.end_warranty > self.start_date_use:
#                 number_days_warranty = self.end_warranty - self.start_date_use
#             else:
#                 number_days_warranty = timedelta(days=0)
#             return number_days_warranty.days
#     number_days_warranty.fget.short_description = 'Остлось дней гарантии'

#     def __str__(self):
#         return self.name
#TODU Гарантия и ремонты: кто принес, когда принес, что случилось и т.д.

class ViewMonitoringObject(models.Model):
    view_name = models.CharField(max_length=100, unique=True, verbose_name = "Вид")

    def __str__(self):
        return self.view_name
    
    class Meta:
	    verbose_name_plural = "Вид объекта"


class TypeMonitoringObject(models.Model):
    type_name = models.CharField(max_length=100, verbose_name = "Тип")
    view = models.ForeignKey(ViewMonitoringObject, on_delete = models.CASCADE, verbose_name = "Вид")

    def __str__(self):
        return f'{self.type_name} {self.view}'
    
    class Meta:
	    verbose_name_plural = "Тип объекта"


class BaseMonitoringObject(models.Model):
    id_number = models.CharField(max_length=12, unique=True, editable=False, verbose_name = "Уникальный номер")
    name = models.CharField(max_length=100, unique=True, verbose_name = "Наименование")
    type = models.ForeignKey(TypeMonitoringObject, on_delete = models.CASCADE, verbose_name = "Тип")
    create_date = models.DateField(auto_now_add=True, null=True, editable=False, verbose_name = "Дата создания")

    def save(self, *args, **kwargs) -> None:
        if not self.id_number:
            now_time = str(time.time())
            self.id_number = f'{now_time[:5]}-{now_time[5:10]}'
        super(BaseMonitoringObject, self).save(*args, **kwargs)
    
# import string
# import random

# def random_numstr(len:int)->str:
#     char_list = random.choices(string.digits, k=len)
#     return "".join(char_list)

    def __str__(self):
        return f'{self.id_number}  {self.type} "{self.name}"'

    class Meta:
	    verbose_name_plural = "Базовый класс"


class Production(models.Model):
    date_production = models.DateField(verbose_name = "Дата производства")
    user = models.CharField(max_length=100, verbose_name = "Пользователь")
    object = models.ForeignKey(BaseMonitoringObject, on_delete=models.CASCADE, verbose_name = "Продукт")

    def __str__(self):
        return str(self.date_production)
