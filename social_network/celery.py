import os

from celery import Celery
from celery.schedules import crontab
from console.jobs import queue_job
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_network.settings')

app = Celery('social_network')

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.beat_schedule = {
#     'print_jobs_3s':{
#         'task':'console.jobs.queue_job.print_jobs',
#         'schedule': crontab(minute='*/1'),
#         'args':()
#     }
# }

app.autodiscover_tasks()

# celery -A social_network beat -l INFO
# celery -A social_network worker -l INFO