from django.core.management.base import BaseCommand

from yandex_weather_app.models import Town


class Command(BaseCommand):
    help = 'Delete towns'

    def handle(self, *args, **kwargs):

        Town.objects.all().delete()
