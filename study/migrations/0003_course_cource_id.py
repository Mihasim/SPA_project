# Generated by Django 4.2.8 on 2023-12-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cource_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='id курса'),
        ),
    ]
