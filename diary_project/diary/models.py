from django.db import models

class DiaryEntry(models.Model):
    date = models.DateField()
    event = models.CharField(max_length=200)
    feelings = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.event}"



