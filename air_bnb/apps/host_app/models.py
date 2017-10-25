# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import Users


# Create your models here.

# class ListingManager(models.Manager):

class Venues(models.Model):
    host_id = models.ForeignKey(Users, null=True, blank=True)
    space_name = models.CharField(max_length=255)
    dry_zone = models.CharField(max_length=5)
    noise_level = models.CharField(max_length=255)
    capacity = models.IntegerField()
    overnight_option = models.CharField(max_length=5)
    suggested_donation = models.CharField(max_length=5)
    promotions = models.CharField(max_length=5)
    gear_availability = models.TextField()
    show_start = models.TimeField()
    show_end = models.TimeField()
    bill_capacity = models.CharField(max_length=255)
    location_type = models.CharField(max_length=255)
    past_performers = models.TextField(null=True)
    street_address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shows(models.Model):
    venue_id = models.ForeignKey(Venues)
    bands = models.TextField()
    show_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reviews(models.Model):
    venue_id = models.ForeignKey(Venues)
    musicians_id = models.ForeignKey(Users)
    rating = models.IntegerField()
    review_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)