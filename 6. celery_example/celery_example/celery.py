from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from email_example import tasks

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_example.settings')

app = Celery('celery_example')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     'populate-every-monday': {
#         'task': 'tasks.sleepy_sum',
#         'schedule': crontab(hour=3, minute=33, day_of_week=4),
#         'args': (16,)
#     }
# }


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
