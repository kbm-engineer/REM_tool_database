# Generated by Django 4.2.3 on 2023-08-07 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0018_uniqueidentificator_alter_basemonitoringobject_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniqueidentificator',
            name='nomber',
            field=models.TextField(blank=True, max_length=16, unique=True),
        ),
    ]
