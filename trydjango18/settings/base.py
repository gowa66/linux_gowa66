"""
Django settings for trydjango18 project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ecqlugw4v_gm_e6dd35b-8)e0u=j7h=2a1d*ts$c&*0w8g2@8j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gover66at@gmail.com'
EMAIL_HOST_PASSWORD = 'govergowa62236'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Application definition

INSTALLED_APPS = (
    #django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_comments',
    
    #third party apps
    'crispy_forms',
    'registration',
    
    
    #my apps
    'newsletter',
    'blog',
    'user_profile',
    'djangoChat',
    'portfolio',
  
    
    
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

# GOOGLE_OAUTH2_CLIENT_ID = '894617274061-4b1at0bcuccnftki3ntopv73c41s5ru3.apps.googleusercontent.com'

# GOOGLE_OAUTH2_CLIENT_SECRET = '4E8BuWLfqInGx04lrySkQRjq'

# FACEBOOK_APP_ID = '1479681382337084'
# FACEBOOK_API_SECRET = '4570fbb58e397e8f4f1d7010afec54e5'
# FACEBOOK_EXTENDED_PERMISSIONS = ['email']

# AUTHENTICATION_BACKENDS = (
#                             'social_auth.backends.google.GoogleOAuth2Backend',
#                             'social_auth.backends.facebook.FacebookBackend',
#                             'django.contrib.auth.backends.ModelBackand',
#                             )


ROOT_URLCONF = 'trydjango18.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'trydjango18.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "static_root")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_in_pro", "our_static"),
    os.path.join(BASE_DIR, "static_in_env"),
    # '/var/www/static/',
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")

MEDIAFILES_DIRS = (
    os.path.join(BASE_DIR, "static_in_pro", "our_static"),
    os.path.join(BASE_DIR, "static_in_env"),

)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#crispy from tags set
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#django registr redux set
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

