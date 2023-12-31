# Generated by Django 4.2.8 on 2023-12-24 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_payments_date_payments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Сылка на оплату'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='date_payments',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 14, 50, 19, 677090), verbose_name='дата оплаты'),
        ),
    ]
