from django.contrib import admin

from diary.models import DiaryEntry


@admin.register(DiaryEntry)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'date', 'event', 'feelings'
    ]
