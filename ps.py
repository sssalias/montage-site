# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u2795968/data/www/sharazhmontazh.com/project_name')
sys.path.insert(1, '/var/www/u2795968/data/djangoenv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'project_name.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()