from .common import *



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lr#&kxg)3g91o@hc_s52u2h424w#u^wu57sf%burm)kx(29x0&'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'symport',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Lailaha4'
    }
}

SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY

GOOGLE_API_KEY = '/Users/sm/Desktop/comp sci/personal projects/APIkeys/GoogleAPI.txt'

EMAIL_USER_DIR = '/Users/sm/Desktop/comp sci/personal projects/APIkeys/email_address.txt'
EMAIL_PASS_DIR = '/Users/sm/Desktop/comp sci/personal projects/APIkeys/email_password.txt'
