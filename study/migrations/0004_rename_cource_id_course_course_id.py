# Generated by Django 4.2.8 on 2023-12-24 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_course_cource_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='cource_id',
            new_name='course_id',
        ),
    ]