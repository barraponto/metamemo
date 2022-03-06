import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "metamemo.settings")

app = Celery("metamemo")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
