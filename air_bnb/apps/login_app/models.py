# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
EMAIL_REGEX = re.compile("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$")

class UserManager(models.Manager):
    def registration_validation(self, postData):
        errors = []
        if len(postData['first_name']) < 2 or any(str.isdigit(char) for char in str(postData['first_name'])):
            errors.append('First name must contain only letters and be at least two characters')
        if len(postData['last_name']) < 2 or any(str.isdigit(char) for char in str(postData['last_name'])):
            errors.append('Last name must contain only letters and be at least two characters')
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Email not valid')
        try:
            Users.objects.get(email=postData['email'])
            errors.append('A user already has this email')
        except:
            pass
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters')
        if postData['password'] != postData['confirmed_password']:
            errors.append('Please make sure your passwords match!')
        return errors

    def login_validation(self, postData):
        errors = []
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Please enter a valid email!')
        if len(postData['email']) < 1:
            errors.append('Please enter an email')
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters')
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()