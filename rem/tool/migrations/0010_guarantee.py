# Generated by Django 4.2.3 on 2023-08-18 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0009_remove_basemonitoringobject_days_warranty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guarantee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tool.basemonitoringobject')),
            ],
        ),
    ]
