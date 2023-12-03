from django.contrib import admin

from yandex_weather_app.models import Town


@admin.register(Town)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
