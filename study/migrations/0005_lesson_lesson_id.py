# Generated by Django 4.2.8 on 2023-12-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_rename_cource_id_course_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='id курса'),
        ),
    ]