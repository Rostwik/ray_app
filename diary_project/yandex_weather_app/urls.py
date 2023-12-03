from django.urls import path

from yandex_weather_app import views

urlpatterns = [
    path('weather/', views.weather, name='weather'),
]
