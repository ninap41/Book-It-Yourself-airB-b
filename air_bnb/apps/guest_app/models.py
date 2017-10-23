# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..trips_app.models import Listings
from ..login_app.models import Users
# Create your models here.

class Photos(models.Model):
    listing_id = models.ForeignKey(Listings)
    user_id = models.ForeignKey(Users)
    photo = models.ImageField()