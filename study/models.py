from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название курса')
    preview = models.ImageField(upload_to='course_preview/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(upload_to='lesson_preview/', verbose_name='Превью', **NULLABLE)
    link_on_video = models.TextField(verbose_name='Ссылка на видео', **NULLABLE)
    course_lesson = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


