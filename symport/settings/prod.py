import os
import dj_database_url
# from symport.settings.dev import SECRET_KEY
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DATABASES = {
    'default': dj_database_url.config()
    
}
SECRET_KEY = os.environ['SECRET_KEY']

GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

EMAIL_USER_DIR = ['EMAIL_USER']
EMAIL_PASS_DIR = ['EMAIL_PASS']

ALLOWED_HOSTS = ['symport-prod.herokuapp.com']

SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY