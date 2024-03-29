import os
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-s^hgko+3b9#6&utnfh%dd7551=5@vz&&+9k6!%n77a8cze@w9q'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_celery_beat',

    'drf_yasg',

    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',

    'study',
    'users',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Настройки JWT-токенов
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',  # Кому предоставлен доступ AllowAny не накладывает никаких ограничений
    ),

}

# Настройки срока действия токенов
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'study',
        'USER': 'postgres',
        'PASSWORD': '5482',
        'HOST': 'db',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'users.User'

# Настройки для Celery
# URL-адрес брокера сообщений
CELERY_BROKER_URL = 'redis://redis:6379/0'  # Например, Redis, который по умолчанию работает на порту 6379
# URL-адрес брокера результатов, также Redis
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
# Часовой пояс для работы Celery
CELERY_TIMEZONE = "Australia/Tasmania"
# Флаг отслеживания выполнения задач
CELERY_TASK_TRACK_STARTED = True
# Максимальное время на выполнение задачи
CELERY_TASK_TIME_LIMIT = 30 * 60

# Настройки для Celery_BEAT
CELERY_BEAT_SCHEDULE = {
    'check_user_last_login': {
        'task': 'study.tasks.check_user_last_login',  # Путь к задаче
        'schedule': timedelta(seconds=10),  # Расписание выполнения задачи (например, каждые 10 секунд)
    },
}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'mihasim251@yandex.ru'
EMAIL_HOST_PASSWORD = 'auiswsqruziryjki'
EMAIL_USE_SSL = True
