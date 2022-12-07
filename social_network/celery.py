import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_network.settings')

app = Celery('social_network')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'print_jobs_3s':{
        'task':'api_app.tasks.print_jobs',
        'schedule': 3.0
    }
}

app.autodiscover_tasks()

# celery -A social_network beat -l INFO
# celery -A social_network worker -l INFO