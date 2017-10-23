# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import Users

# Create your models here.

class Listings(models.Model):
    host_id = models.ForeignKey(Users)
    guest_size = models.IntegerField()
    listing_size = models.CharField(max_length=255)
    property_type = models.CharField(max_length=255)
    amount_of_bedrooms = models.IntegerField()
    amount_of_beds = models.IntegerField()
    bed_size = models.CharField(max_length=255)
    amount_of_bathrooms = models.IntegerField()
    country = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    apt_number = models.IntegerField(null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    house_amenities = models.TextField(null=True)
    safety_amenities = models.TextField(null=True)
    available_spaces = models.TextField(null=True)
    description = models.TextField()
    house_rules = models.TextField(null=True)
    cancellation_policy = models.TextField(null=True)
    listing_name = models.CharField()
    per_night_charge = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Trips(models.Model):
    listing_id = models.ForeignKey(Listings)
    guests = models.ForeignKey(Users)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


