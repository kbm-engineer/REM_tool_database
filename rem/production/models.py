from django.db import models
from organization.models import Organization, CustomUser
import uuid


class QRCode(models.Model):
    unique_number = models.CharField(max_length=6, unique=True, editable=False, verbose_name = "Уникальный номер", blank=True, null=True)

    def save(self, *args, **kwargs) -> None:
        if not self.unique_number:
            self.unique_number = str(uuid.uuid4().int)[:10]
        super(QRCode, self).save(*args, **kwargs)

    def __str__(self):
        return self.unique_number
    
    class Meta:
	    verbose_name_plural = "Уникальная регистрация"


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


class Parametrs(models.Model):
    pass


class Production(models.Model):
    create_date = models.DateField(auto_now_add=True, null=True, verbose_name = "Дата производства")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True, verbose_name = "Организация")
    collector = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name = "Сборщик")


    def __str__(self):
        return str(self.create_date)
    
    class Meta:
	    verbose_name_plural = "Производство"


class BaseMonitoringObject(models.Model):
    qrcode = models.ForeignKey(QRCode, on_delete=models.CASCADE, verbose_name = "QRcode", blank=True, editable=False, null=True)
    name = models.CharField(max_length=100, verbose_name = "Наименование")
    type = models.ForeignKey(TypeMonitoringObject, on_delete = models.CASCADE, verbose_name = "Тип")
    production = models.ForeignKey(Production, on_delete=models.CASCADE, verbose_name = "Производство", blank=True, null=True)
    active = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.qrcode:
            super().save(*args, **kwargs)
            self.qrcode = QRCode.objects.create()
            self.save(update_fields=['qrcode'])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.qrcode.unique_number} - {self.name}'

    class Meta:
	    verbose_name_plural = "Базовый класс"
