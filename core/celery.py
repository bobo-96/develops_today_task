import os
from celery.schedules import crontab
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    "reset_upvote": {
        "task": "apps.posts.tasks.reset_upvote",
        "schedule": crontab(),
# minute=10, hour=25
    }
}