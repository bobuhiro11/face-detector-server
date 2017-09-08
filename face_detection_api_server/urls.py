from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^face_detection/', include('face_detection.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('face_detection_rest.urls', namespace='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)