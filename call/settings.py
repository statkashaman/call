import os
import os.path

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = 'askq/static/'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
TEMPLATE_DIRS = (
    'askq/templates/askq',
)

SECRET_KEY = '12@z+rk+m_ec-f^76v=&m4^#sxj@9212*$=oh_i)t_mtk9p%%_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['call.bis.local']

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.formtools',
    'django.contrib.admin',
    'askq',
    'django_cleanup',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'call.urls'

WSGI_APPLICATION = 'call.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'bis077',
        'HOST': '192.168.0.196',
        'PORT': '3306',
    }
}

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Novosibirsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True
