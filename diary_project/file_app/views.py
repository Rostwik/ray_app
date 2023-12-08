from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from rest_framework.parsers import FileUploadParser
from file_app.tasks import process_files


class GetFilesList(APIView):
    def get(self, request):
        queryset = File.objects.all()
        serializer_for_queryset = FileSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)


class UploadFileView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            process_files.delay()
            # process_files.delay()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
