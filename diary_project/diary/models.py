from django.db import models
from django.contrib.auth.models import User


class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    event = models.CharField(max_length=200)
    feelings = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.date} - {self.event}"
