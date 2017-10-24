# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..host_app.models import Listings
from ..login_app.models import Users
# Create your models here.

# class MusicianManager(models.Model):

class Photos(models.Model):
    listing_id = models.ForeignKey(Listings)
    user_id = models.ForeignKey(Users)
    photo = models.ImageField()

class Musicians(models.Model):
    musician_id = models.ForeignKey(Users)
    name = models.CharField(max_length=255)
    other_profiles = models.TextField()
    email = models.CharField(max_length=255)
    bio = models.TextField()

    