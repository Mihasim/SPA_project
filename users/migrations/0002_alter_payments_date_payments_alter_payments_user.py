# Generated by Django 4.2.8 on 2023-12-22 11:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='date_payments',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 22, 11, 33, 3, 593592), verbose_name='дата оплаты'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]