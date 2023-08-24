# Generated by Django 4.2.3 on 2023-08-22 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0003_alter_basemonitoringobject_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemonitoringobject',
            name='qrcode',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='tool.qrcode', verbose_name='QRcode'),
            preserve_default=False,
        ),
    ]
