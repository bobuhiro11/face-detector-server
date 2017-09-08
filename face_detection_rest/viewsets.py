from rest_framework import viewsets, filters
from face_detection_rest.serializers import UploadedImageSerializer # import our serializer
from face_detection.models import UploadedImage # import our model


class UploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer