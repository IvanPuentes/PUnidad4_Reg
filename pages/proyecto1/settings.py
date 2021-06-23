"""
Django settings for proyecto1 project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path,os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-9ndg2jy1yh!_=uo53k5e@+)76oge0x0e1272yrz57ovkoqd2q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

#------------------------------------#

ACCOUNT_EMAIL_VERIFICATION = True

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_USERNAME_REQIRED = False


ACCOUNT_AUTHENTICATION_METHOD = 'email'
#-----------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ivan.puentes2525@gmail.com'
EMAIL_HOST_PASSWORD = 'Hola1234@'
EMAIL_USE_TLS = True




# Application definition

INSTALLED_APPS = [
    'mipagina.apps.MipaginaConfig',
    'orders.apps.OrdersConfig',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'social_django',
   
   
]

SITE_ID = 1


TIME_ZONE='America/Monterrey'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware', 
]

ROOT_URLCONF = 'proyecto1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [os.path.join(BASE_DIR,'templates')],#new
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


WSGI_APPLICATION = 'proyecto1.wsgi.application'

AUTHENTICATION_BACKENDS = [
   
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.github.GithubOAuth2',


]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER':'postgres',
        'PASSWORD':'postgres',
        'HOST':'db',
        'PORT':5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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



# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS= [os.path.join(BASE_DIR, "static")]



MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

AUTH_USER_MODEL = 'mipagina.UsuarioPers'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'home'

STRIPE_TEST_PUBLISHABLE_KEY=os.environ.get('STRIPE_TEST_PUBLISHABLE_KEY')
STRIPE_TEST_SECRET_KEY=os.environ.get('STRIPE_TEST_SECRET_KEY')


SOCIAL_AUTH_GITHUB_KEY = '8422cbadd00f8bb08dc1'
SOCIAL_AUTH_GITHUB_SECRET = '9d04f7eda87924deb45790d8049538ef419f386c'