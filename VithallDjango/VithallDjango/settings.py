"""
Django settings for VithallDjango project.

Based on 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import posixpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '33d439c7-9117-4c08-9517-dd666d3c3484'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    'app',
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    #�������뵼������
    'import_export',
    #��ҳ
    'pure_pagination', 
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'VithallDjango.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'VithallDjango/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'VithallDjango.wsgi.application'
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#��ҳ����
PAGINATION_SETTINGS = {
    # ��ҳ����ǰҳǰ��Ӧ����ʾ����ҳ�������߾��ȷֲ������Ҫ����Ϊż����
    'PAGE_RANGE_DISPLAYED': 4, 
    # ��ҳ����ͷ�ͽ�β��ʾ��ҳ��
    'MARGIN_PAGES_DISPLAYED': 2,
    # �������˲�����ҳ����ʾ��һҳ
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,}

#�л�ΪMysql���ݿ�
#DATABASES = {
#        'default': {
#        'ENGINE': 'django.db.backends.mysql', 
#        'NAME': 'aircraft',    #������ݿ�����
#        'USER': 'root',   #������ݿ��û���
#        'PASSWORD': '123456', #������ݿ�����
#        'HOST': '', #������ݿ�����������Ĭ��Ϊlocalhost
#        'PORT': '3306', #������ݿ�˿�
#    }
#}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    #{
    #    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #},
]

#��֤��¼@login_required��������ָ����¼���ӣ�����Ĭ��������account/login/
LOGIN_URL = '/login/'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')  # ���þ�̬�ļ�·��Ϊ��Ŀ¼�µ�media�ļ���
MEDIA_URL = '/media/'
