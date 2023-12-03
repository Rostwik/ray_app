from django.db import models


class Town(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название города')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    temp = models.IntegerField(verbose_name='Температура', blank=True, null=True)
    wind_speed = models.IntegerField(verbose_name='Скорость ветра', blank=True, null=True)
    pressure_mm = models.IntegerField(verbose_name='Давление', blank=True, null=True)
    request_time = models.DateTimeField(verbose_name='Время запроса', blank=True, null=True)
    is_request = models.BooleanField(verbose_name='Наличие запроса', blank=True, null=True)

    def __str__(self):
        return self.name


class BotState(models.Model):
    chat_id = models.CharField(max_length=100, verbose_name='Телеграм chat_id', blank=True, null=True)
    state = models.CharField(max_length=100, verbose_name='Состояние бота', blank=True, null=True)