import os, sys

sys.path.insert(0, '/home/m/matveye7/matveye7.beget.tech/DevClassroom/DevClassroom')
sys.path.insert(1, '/home/m/matveye7/matveye7.beget.tech/DevClassroom/DevClassVenv/lib/python3.11/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'DevClassroom.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()