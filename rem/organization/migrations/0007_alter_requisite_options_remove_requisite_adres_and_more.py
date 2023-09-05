# Generated by Django 4.2.3 on 2023-08-30 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_remove_requisite_name_organization_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requisite',
            options={'verbose_name_plural': 'Банковские реквизиты'},
        ),
        migrations.RemoveField(
            model_name='requisite',
            name='adres',
        ),
        migrations.RemoveField(
            model_name='requisite',
            name='telephone',
        ),
        migrations.AddField(
            model_name='organization',
            name='adres',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.adres', verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='organization',
            name='telephone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='requisite',
            name='inn_nomber',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]
