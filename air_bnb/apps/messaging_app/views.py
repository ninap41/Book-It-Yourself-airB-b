# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def inbox(request):
        return render(request, "messaging_app/inbox.html")
        
