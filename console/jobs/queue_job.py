from celery import shared_task
# from social_network.celery import app

@shared_task
def print_jobs():
    return 'hello world'