from rest_framework import serializers

from study.models import Course, Lesson, Payments


class LessonSerializer(serializers.ModelSerializer):
    """
    Сереализатор для уроков
    """
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """
    Сереализатор для курсов
    """
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        """
        Функция для получения количества уроков
        """
        return Lesson.objects.filter(course_lesson=obj.id).count()




class PaymentsSerializer(serializers.ModelSerializer):
    """
    Сереализатор для платежей
    """
    class Meta:
        model = Payments
        fields = '__all__'
