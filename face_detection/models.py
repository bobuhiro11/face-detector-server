from django.db import models


class UploadedImage(models.Model):
  data = models.ImageField(upload_to='original_images')
