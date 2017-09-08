from django.db import models


class UploadedImage(models.Model):
  data = models.ImageField(upload_to='uploaded_images')
