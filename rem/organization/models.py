from django.db import models
from django.contrib.auth.models import AbstractUser


class Adres(models.Model):
    city = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name = 'Город'
    )
    street = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name = 'Улица'
    )
    house = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name = 'Дом'
    )
    index = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name = 'Индекс'
    )

    def __str__(self):
        return f'{self.city}, {self.street}, {self.house}'

    class Meta:
	    verbose_name_plural = "Адреса фирм"


class Requisite(models.Model):
    inn_nomber = models.IntegerField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='ИНН',
    )
    
    def __str__(self):
        return f'ИНН: {str(self.inn_nomber)}'

    class Meta:
	    verbose_name_plural = "Банковские реквизиты"


class Organization(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name = 'Наименование',
        unique=True,
    )
    telephone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name = 'Телефон'
    )
    requisite = models.ForeignKey(
        Requisite,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name = 'Банковские реквизиты'
    )
    adres = models.ForeignKey(
        Adres,
        on_delete=models.CASCADE,
        verbose_name = 'Адрес',
        blank=True,
        null=True
    )
    active = models.BooleanField(
        default=False,
        verbose_name = 'Активация'
    )

    def __str__(self):
        return self.name

    class Meta:
	    verbose_name_plural = "Организации"


class CustomUser(AbstractUser):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Организация',
    )