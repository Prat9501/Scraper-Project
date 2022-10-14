from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
#from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraper.settings')

app = Celery('scraper')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'every-10-seconds' : {
        'task': 'crypto.tasks.update_details',
        'schedule': 5,
    },
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')