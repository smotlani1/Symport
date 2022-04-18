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

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

EMAIL_USER = os.environ['EMAIL_USER']
EMAIL_PASS = os.environ['EMAIL_PASS']

ALLOWED_HOSTS = ['symport-prod.herokuapp.com']

SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY