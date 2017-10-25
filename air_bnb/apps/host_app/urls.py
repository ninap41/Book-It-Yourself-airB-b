from django.conf.urls import url
from django.contrib import admin
from . import views
  
urlpatterns = [
        url(r'^add_host$', views.add_host),
        url(r'^create_venue$', views.create_venue),
        
  ]