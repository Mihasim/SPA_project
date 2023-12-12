from django.contrib import admin

from study.models import Course, Lesson, Payments

admin.site.register(Course)

admin.site.register(Lesson)

admin.site.register(Payments)

