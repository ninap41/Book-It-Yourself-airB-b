# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import Users
from ..host_app.models import Listings

# Create your models here.

# class ShowManager(models.Manager):
# class ReviewManager(models.Manager):

class Shows(models.Model):
    listing_id = models.ForeignKey(Listings)
    musicians = models.ForeignKey(Users)
    show_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reviews(models.Model):
    listing_id = models.ForeignKey(Listings)
    musicians_id = models.ForeignKey(Users)
    rating = models.IntegerField()
    review_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


