# Generated by Django 4.2.3 on 2023-08-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_customuser_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisite',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Наименование'),
        ),
    ]
