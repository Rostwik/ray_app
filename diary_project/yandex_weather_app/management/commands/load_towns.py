from django.core.management.base import BaseCommand

from yandex_weather_app.models import Town


class Command(BaseCommand):
    help = 'Add towns'

    def handle(self, *args, **kwargs):
        with open('towns_coordinates.txt', encoding='utf-8', mode='r') as file:
            towns_list = [line.split('—') for line in file]
            towns = {town[0].strip(): town[1].strip() for town in towns_list}

        bulk_list = list()
        for town_name, coord in towns.items():
            lat, lon = coord.split(',')

            bulk_list.append(
                Town(name=town_name, lat=lat.strip(), lon=lon.strip())
            )

        Town.objects.bulk_create(bulk_list)
