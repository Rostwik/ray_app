
from celery import shared_task

from .models import File


@shared_task()
def process_files():
    for file in File.objects.filter(processed=False):
        file.processed = True
        file.save()
        return True
    return False
