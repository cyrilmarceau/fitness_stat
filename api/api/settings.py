"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import ast

from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

def get_bool_from_env(name, default_value):
    if name in os.environ:
        value = os.environ[name]
        try:
            return ast.literal_eval(value)
        except ValueError as e:
            raise ValueError("{} is an invalid value for {}".format(value, name)) from e
    return default_value


# ENV VARIABLES

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = str(os.getenv('SECRET_KEY'))

APP_NAME = str(os.getenv('APP_NAME', 'Fitness stat'))

## DEBUG VARIABLES
DEBUG = True if str(os.getenv('DJANGO_MODE')) == "development" else False
DEBUG_EMAIL = get_bool_from_env("DEBUG_EMAIL", False)

# CORS
ALLOWED_HOSTS = [
    '0.0.0.0',
    '192.168.1.29',
    '192.168.20.214'
]

CORS_ORIGIN_WHITELIST = [
    'exp://192.168.1.29:19000',  # Local
    'exp://192.168.20.214:19000'  # Ecole
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'rest_framework',

    # Auth
    # 'rest_framework_simplejwt.token_blacklist',
    'allauth',
    'allauth.account',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    # App
    'core.apps.CoreConfig',
    'app_api',
]

# --------- EMAIL CONFIG ---------

SUBJECT_EMAIL = {
    'new_user': f"Bienvenue sur l'application {APP_NAME}"
}

if DEBUG_EMAIL:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "mailhog"
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = None
    EMAIL_HOST_PASSWORD = None
    EMAIL_USE_TLS = False

# --------- PACKAGES CONFIG ---------

# DJ-REST-AUTH CONFIG
SITE_ID = 1

## AUTHENTIFICATION
REST_AUTH_TOKEN_MODEL = None
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'

## Overide serializer
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'app_api.serializers.CustomUserDetailsSerializer',
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'app_api.serializers.CustomRegisterSerializer'
}

# DJANGO EMAIL FROM
DEFAULT_FROM_EMAIL = os.environ.get("MAILGUN_SENDER_EMAIL_FROM", "app@fitness-stat.com")

#  DJANGO-ALLAUTH
ACCOUNT_ADAPTER = 'app_api.adaptater.DefaultAccountAdapterCustom'  # Override activate_url
ACCOUNT_EMAIL_REQUIRED = True # must verify email when signup
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Must verify account email
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''  # Disable default prefix
ACCOUNT_CONFIRM_EMAIL_ON_GET = False  # Manually press button for validate account
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1  # Expiration email link in day

if DEBUG:
    LOGIN_URL = 'http://0.0.0.0:9010/public/auth/account-validate/'
else:
    LOGIN_URL = 'http://0.0.0.0:9010/public/auth/account-validate/'

# JWT
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id'
}

# --------- DJANGO AND DJANGO_REST CONFIG ---------

PASSWORD_RESET_TIMEOUT = 86400 # email link available for 1 day

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "public_api/templates/")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'api.context_processors.custom_variables'
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'

# Database
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': str(os.getenv('DB_NAME')),
        'USER': str(os.getenv('DB_USER')),
        'PASSWORD': str(os.getenv('DB_PASSWORD')),
        'HOST': str(os.getenv('DB_HOST')),
        'PORT': str(os.getenv('DB_PORT')),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# Password validation

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{asctime} - {levelname} :: {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'app_api': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'core': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'core.User'
