# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..host_app.models import Venues, Shows
from ..login_app.models import Users
from ..musician_app.models import Musicians

# Create your views here.
def venues(request):
        context = {
                'venues': Venues.objects.all()
        }
        return render(request, 'shows_app/show_list.html', context)

def venue_profile(request, venue_id):
        current_user = Users.objects.get(id=request.session['user_id'])
        current_venue = Venues.objects.get(host_id=current_user)
        context = {
                'venue': Venues.objects.get(id=venue_id),
                'shows': Shows.objects.filter(venue_id=venue_id)
        }
        return render(request, 'shows_app/venue_profile.html', context)

def add_show(request):
        current_user = Users.objects.get(id=request.session['user_id'])
        current_venue = Venues.objects.get(host_id=current_user)
        show_date = request.POST['show_date']
        bands = request.POST['bands']
        Shows.objects.create(venue_id=current_venue, show_date=show_date, bands=bands)
        return redirect('/shows/venues/{}'.format(current_venue.id) )

def delete_show(request, show_id):
        current_user = Users.objects.get(id=request.session['user_id'])
        current_venue = Venues.objects.get(host_id=current_user)
        Shows.objects.get(id=show_id).delete()
        return redirect('/shows/venues/{}'.format(current_venue.id))

def join_show(request, show_id):
        current_user = Users.objects.get(id=request.session['user_id'])
        current_venue = Venues.objects.get(host_id=current_user)
        show = Shows.objects.get(id=show_id)
        print show.show_date
        print current_venue.space_name
        context = {
                'show': show,
                'venue': current_venue
                # 'user': Users.objects.get(id=request.session['user_id'])
        }
        print current_user.type_of_user
        return render(request, 'shows_app/join_show.html', context)

def band_submission(request):
        current_user = Users.objects.get(id=request.session['user_id'])
        musician_id = current_user
        artist_name = request.POST['artist_name']
        other_profiles = request.POST['other_profiles']
        email = request.POST['email']
        bio = request.POST['bio']
        current_band = Musicians.objects.get(musician_id=current_user)
        if current_band:
                current_band.artist_name = request.POST['artist_name']
                current_band.other_profiles = request.POST['other_profiles']
                current_band.email = request.POST['email']
                current_band.bio = request.POST['bio']
                current_band.save()
        else:
                Musicians.objects.create(musician_id=musician_id, artist_name=artist_name, other_profiles=other_profiles, email=email, bio=bio)
        if current_user.type_of_user == 3 or current_user.type_of_user == 4:
                current_user.type_of_user = 4
                current_user.save()
        else:
                current_user.type_of_user = 2
        current_user.save()

        print Musicians.objects.all().values()
        return redirect('/shows')