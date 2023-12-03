from django.urls import path

from .views import GetFilesList, UploadFileView


app_name = "file_app"

urlpatterns = [
    path('files', GetFilesList.as_view()),
    path('upload', UploadFileView.as_view()),
]
