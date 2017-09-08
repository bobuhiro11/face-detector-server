from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image # For ImageFile uploader.


def index(request):
    return HttpResponse("Hello, Welcome to Face Detection API Server.")
