from rest_framework import serializers

from study.models import Course, Lesson
from study.validators import LinkValidator
from users.models import UserSubscriptions
from users.serializers import UserSubscriptionSerializer


class LessonSerializer(serializers.ModelSerializer):
    """
    Сереализатор для уроков
    """


    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link_on_video')]




class CourseSerializer(serializers.ModelSerializer):
    """
    Сереализатор для курсов
    """
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscribers_count = serializers.SerializerMethodField(read_only=True)
    subscribers = UserSubscriptionSerializer(source='usersubscriptions_set', many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        """
        Функция для получения количества уроков
        """
        return Lesson.objects.filter(course_lesson=obj.id).count()

    def get_subscribers_count(self, obj):
        """
        Функция для получения количества подписчиков
        """

        return UserSubscriptions.objects.filter(course=obj.id).count()

    def get_is_subscribed(self, obj):
        """
        Функция для получения признака подписки
        """
        request = self.context.get('request')
        #print(request.user.email)
        #print(obj)
        print(UserSubscriptions.objects.all())
        #print(request.user.email)
        print(request.user.pk)
        subscribers_set = UserSubscriptions.objects.filter(course=obj)
        #if UserSubscriptions.objects.filter(course=obj.id) == True:
        #    print("Подписан")
        #    return True
        return False


