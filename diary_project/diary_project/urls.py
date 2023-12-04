from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include('file_app.urls')),
    path('ya_api/', include('yandex_weather_app.urls')),
]