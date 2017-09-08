from rest_framework import serializers
from face_detection.models import UploadedImage # Import our UploadedImage model


class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ('pk', 'image', ) # only serialize the primary key and the image field