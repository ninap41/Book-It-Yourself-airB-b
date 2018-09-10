from django.conf.urls import url
from django.contrib import admin
from . import views
  
urlpatterns = [
    
        url(r'^$', views.venues),
        url(r'^venues$', views.venue_profile),
        url(r'^venues/(?P<venue_id>\d+)$', views.venue_profile),
        url(r'^venues/host/(?P<host_id>\d+)$', views.host_profile),
        url(r'^delete_venue/(?P<venue_id>\d+)$', views.delete_venue),
        # need to add a show id to the end of the join url
        url(r'^add_show$', views.add_show),
        url(r'^inbox$', views.inbox),
        url(r'^delete_show/(?P<show_id>\d+)$', views.delete_show),
        url(r'^create_review/(?P<venue_id>\d+)$', views.create_review),
        url(r'^join/(?P<venue_id>\d+)/(?P<show_id>\d+)$', views.join_show),
        url(r'^band_submission/(?P<venue_id>\d+)/(?P<show_id>\d+)$', views.band_submission),
        url(r'^accept_band/(?P<venue_id>\d+)/(?P<show_id>\d+)/(?P<musician_id>\d+)$', views.accept_band),
        url(r'^deny_band/(?P<venue_id>\d+)/(?P<musician_id>\d+)$', views.deny_band),
  ]