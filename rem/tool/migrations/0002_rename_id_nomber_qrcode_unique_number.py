# Generated by Django 4.2.3 on 2023-08-22 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qrcode',
            old_name='id_nomber',
            new_name='unique_number',
        ),
    ]
