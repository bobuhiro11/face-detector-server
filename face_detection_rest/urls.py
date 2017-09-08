from django.conf.urls import url, include
from rest_framework import routers
from face_detection_rest.viewsets import UploadedImagesViewSet
from face_detection_rest import viewsets

router = routers.DefaultRouter()
router.register('images', UploadedImagesViewSet, 'images')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]