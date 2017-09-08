# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 07:34
from __future__ import unicode_literals

from django.db import migrations, models
import face_detection.models


class Migration(migrations.Migration):

    dependencies = [
        ('face_detection', '0006_auto_20170908_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(upload_to=face_detection.models.scramble_uploaded_filename, verbose_name='Uploaded image'),
        ),
    ]
