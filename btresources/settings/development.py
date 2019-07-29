from btresources.settings.common import *




SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '!we0ag^yw*a)3(!vqq3iab%s5enj1#plikv2qo8cp(tzi891ve')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'


ALLOWED_HOSTS = ['127.0.0.1']

 
