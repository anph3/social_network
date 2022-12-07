from celery import shared_task

@shared_task
def print_jobs():
    return 'hello world'