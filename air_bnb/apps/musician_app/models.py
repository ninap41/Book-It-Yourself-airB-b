# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import Users
from ..host_app.models import Venues, Shows

# Create your models here.

# class MusicianManager(models.Model):

class Photos(models.Model):
    venue_id = models.ForeignKey(Venues)
    user_id = models.ForeignKey(Users)
    photo = models.ImageField()

class Musicians(models.Model):
    show_id = models.ForeignKey(Shows, null=True)
    musician_id = models.ForeignKey(Users)
    artist_name = models.CharField(max_length=255)
    other_profiles = models.TextField()
    email = models.CharField(max_length=255)
    bio = models.TextField()

    