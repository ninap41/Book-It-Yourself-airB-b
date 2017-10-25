# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..host_app.models import Venues
from ..login_app.models import Users

# Create your views here.
def venues(request):
        context = {
                'venues': Venues.objects.all()
        }
        return render(request, 'shows_app/show_list.html', context)

def venue_profile(request, venue_id):
        context = {
                'venue': Venues.objects.get(id=venue_id)
        }
        return render(request, 'shows_app/venue_profile.html', context)

def join_show(request):
        return render(request, 'shows_app/join_show.html')

def band_submission(request):
        # current_user = Users.objects.get(id=request.session['user_id']) 
        # remember to change User.type_of_user to 2 upon submission to indicate they are a musician
        current_user = Users.objects.get(id=request.session['user_id'])
        current_user.type_of_user = 2
        current_user.save()
        return redirect('/shows')