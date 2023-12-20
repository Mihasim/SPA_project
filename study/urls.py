from django.urls import path

from study.apps import StudyConfig
from rest_framework.routers import DefaultRouter

from study.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
  LessonUpdateAPIView, LessonDestroyAPIView

app_name = StudyConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
  # lesson
  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
] + router.urls
