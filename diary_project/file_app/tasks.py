from celery import shared_task

from file_app.models import File

from celery.utils.log import get_task_logger

from diary.models import DiaryEntry

logger = get_task_logger(__name__)


@shared_task()
def process_files():
    try:
        logger.info('opa')
        for file in File.objects.filter(processed=False):
            file.processed = True
            file.save()
    except Exception as e:
        print(e)
