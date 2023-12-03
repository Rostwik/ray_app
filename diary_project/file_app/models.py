from django.db import models
import os
from environs import Env


env = Env()
env.read_env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES_DIR = env('FILES_DIR', 'files/')


class File(models.Model):
    file = models.FileField(upload_to=FILES_DIR)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'file'
        verbose_name_plural = 'files'



