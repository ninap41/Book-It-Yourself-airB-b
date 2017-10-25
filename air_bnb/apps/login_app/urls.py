from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^homepage$', views.homepage),
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^update_user$', views.update_user)

]