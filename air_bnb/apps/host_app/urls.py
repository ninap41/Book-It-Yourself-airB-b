from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
  
urlpatterns = [
        url(r'^add_host$', views.add_host),
        url(r'^create_venue$', views.create_venue),
        # url(r'^simple_upload$', views.simple_upload),  
  ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)