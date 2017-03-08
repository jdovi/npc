"""
Django settings for dovimotors project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os, django, sys

DJANGO_ENV = os.environ.get('DJANGO_ENV') or 'development'

# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

if DJANGO_ENV == 'production':
    BASE_URL = 'dovimotors.herokuapp.com' #CHANGE
    PROTOCOL = 'http'
elif DJANGO_ENV == 'staging':
    BASE_URL = 'dovimotors.herokuapp.com' #CHANGE
    PROTOCOL = 'http'
else:
    BASE_URL = '127.0.0.1:8000'
    PROTOCOL = 'http'

# SECURITY WARNING: don't run with debug turned on in production!
if DJANGO_ENV == 'production':
    DEBUG = False
else:
    DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5z5s61a35!p9k-@jffwo)vvy7%vdq!uw8=lfush*p*xw!&wgn9'

if DJANGO_ENV == 'development':
    ALLOWED_HOSTS = ['.dovimotors.herokuapp.com', #CHANGE
                     '127.0.0.1',
                     ]
else:
    ALLOWED_HOSTS = ['.dovimotors.herokuapp.com',  #CHANGE
                     ]


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'DoviMotorsApp' #CHANGE
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
ROOT_URLCONF = 'dovimotors.urls'

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

WSGI_APPLICATION = 'dovimotors.wsgi.application'

#######################################
#       DATABASE CONFIG               #
#######################################
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
if DJANGO_ENV == 'development':
    NAME = os.environ.get('DOVIMOTORSDB') #CHANGE
    ENGINE = os.environ.get('ENGINE')
    USER = os.environ.get('USER')
    PASSWORD = os.environ.get('PASSWORD')
    HOST = os.environ.get('HOST')
    PORT = os.environ.get('PORT')
    DATABASES = {'default': {
                    'ENGINE': ENGINE,
                    'NAME': NAME,
                    'USER': USER,
                    'PASSWORD': PASSWORD,
                    'HOST': HOST,
                    'PORT': PORT},}
else:
    import dj_database_url
    DATABASES = {}
    DATABASES['default'] =  dj_database_url.config()


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'US/Eastern'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

###############################
#  STATIC FILES CONFIG        #
###############################
if DJANGO_ENV == 'development':
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage' #need S3 for file_upload function
    #STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
else:
    # Always use S3 on staging/production
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') 
AWS_STORAGE_BUCKET_NAME = os.environ.get('DOVIMOTORS_S3BUCKET') #CHANGE
AWS_PRELOAD_METADATA = True

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
if DJANGO_ENV == 'development':
    # Won't generally collect locally, but if we do, collect to here
    STATIC_ROOT = '%s/staticfiles/' % SITE_ROOT
else:
    STATIC_ROOT = '%s/staticfiles/' % SITE_ROOT
    
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
if DJANGO_ENV == 'development':
    # Use this to at least pull css/js/etc. from local folder when no internet available
    #STATIC_URL = '/static/'
    
    #however, need to use the S3 line when creating new customers and need file_upload function
    STATIC_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
else:
    STATIC_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#####################################
#    EMAIL CONFIGURATION            #
#####################################
BUILDINGSPEAK_EMAIL_USERNAME = os.environ.get('BUILDINGSPEAK_EMAIL_USERNAME')
BUILDINGSPEAK_EMAIL_PASSWORD = os.environ.get('BUILDINGSPEAK_EMAIL_PASSWORD')
BUILDINGSPEAK_EMAIL_API_KEY = os.environ.get('BUILDINGSPEAK_EMAIL_API_KEY')

# Mail configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = 'admin@buildingspeak.com'
DEFAULT_FROM_EMAIL = 'admin@buildingspeak.com'
EMAIL_TEMPLATE = os.environ.get('EMAIL_TEMPLATE') or 'sample-template'
if DJANGO_ENV == 'development':
  """
  EMAIL_HOST = 'localhost'
  EMAIL_PORT = os.environ.get('EMAIL_PORT') or 1025
  EMAIL_HOST_USER = ''
  EMAIL_HOST_PASSWORD = ''
  EMAIL_PROVIDER = 'localhost'
  """
  EMAIL_HOST = 'smtp.sendgrid.net'
  EMAIL_PORT = 587
  EMAIL_HOST_USER = BUILDINGSPEAK_EMAIL_USERNAME
  EMAIL_HOST_PASSWORD = BUILDINGSPEAK_EMAIL_PASSWORD
  EMAIL_PROVIDER = 'sendgrid'
  
else:
  EMAIL_HOST = 'smtp.sendgrid.net'
  EMAIL_PORT = 587
  EMAIL_HOST_USER = BUILDINGSPEAK_EMAIL_USERNAME
  EMAIL_HOST_PASSWORD = BUILDINGSPEAK_EMAIL_PASSWORD
  EMAIL_PROVIDER = 'sendgrid'

######################################
#     LOGGING CONFIG                 #
######################################
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
if DJANGO_ENV == 'development':
    bsapp_handlers = ['logfile']  # ['console', 'logfile'] #use empty brackets for no logging
else:
    bsapp_handlers = []
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'debug': {
            'format' : "[%(asctime)s] %(levelname)s %(message)s",
            'datefmt' : "%H:%M:%S"
        },
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        #comment 'logfile' entry out to turn off debugging
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': ('%s/../log/%s.log' % (SITE_ROOT, DJANGO_ENV)),
            'maxBytes': 10000000,
            'backupCount': 2,
            'formatter': 'debug',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'debug'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'BuildingSpeakApp': {
            'handlers': bsapp_handlers,
            'level': 'DEBUG',
            'propagate': False,
        },
        
    }
}



