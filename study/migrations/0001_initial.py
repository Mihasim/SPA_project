# Generated by Django 4.2.8 on 2023-12-22 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название курса')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='course_preview/', verbose_name='Превью')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название урока')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='lesson_preview/', verbose_name='Превью')),
                ('link_on_video', models.TextField(blank=True, null=True, verbose_name='Ссылка на видео')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('course_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]
