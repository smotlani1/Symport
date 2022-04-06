import os

from symport.settings.dev import SECRET_KEY
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['symport-prod.herokuapp.com']