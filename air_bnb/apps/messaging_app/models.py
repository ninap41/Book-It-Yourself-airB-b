# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import Users
from ..trips_app.models import Listings

# Create your models here.

class Messages(models.Model):
    sender = models.ForeignKey(Users)
    receiver = models.ForeignKey(Listings)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)