# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..host_app.models import Venues, Shows, Reviews
from ..login_app.models import Users
from ..musician_app.models import Musicians
from django.contrib import messages
from django.template import Library


# Create your views here.
def venues(request):
        try:
                searchState = True
                city = request.POST['city']
                city[0].upper()+city[1:]
                filtered_venues = Venues.objects.filter(city=city)
                context = {
                        'venues': filtered_venues
                }
                venues_list = venues
                return render(request, 'shows_app/show_list.html', context, searchState)
        except:
                context = {
                        'venues': Venues.objects.all()
                }
                venues_list = venues
                if venues_list == 0:
                        searchState = True
                searchState = True
                return render(request, 'shows_app/show_list.html', context, searchState)
        return render(request, 'shows_app/show_list.html', context, searchState)



def venue_profile(request, venue_id):
        current_user = Users.objects.get(id=request.session['user_id'])
        current_venue = Venues.objects.get(id=venue_id)
        shows = Shows.objects.filter(venue_id=current_venue)
        musicians = [] 
        print Musicians.objects.all().values()
        for show in shows:
                print show.id
                if Musicians.objects.filter(show_id=show.id):
                        band = Musicians.objects.filter(show_id=show.id)
                        musicians.append(band)
        print musicians
        reviews = Reviews.objects.filter(venue_id=venue_id)
        context = {
                'venue': Venues.objects.get(id=venue_id),
                'shows': shows,
                'reviews': reviews,
                'user': current_user,
                'musicians': musicians
        }
        return render(request, 'shows_app/venue_profile.html', context)

def add_show(request):
        current_user = Users.objects.get(id=request.session['user_id'])
        current_venue = Venues.objects.get(host_id=current_user)
        show_date = request.POST['show_date']
        bands = request.POST['bands']
        Shows.objects.create(venue_id=current_venue, show_date=show_date, bands=bands)
        return redirect('/shows/venues/{}'.format(current_venue.id) )

def inbox(request):
        current_user = Users.objects.get(id=request.session['user_id'])
        current_venue = Venues.objects.get(host_id=current_user)
        show_date = request.POST['show_date']
        bands = request.POST['bands']
        Shows.objects.create(venue_id=current_venue, show_date=show_date, bands=bands)
        return render(request, 'messages_app/inbox.html', context)

def delete_show(request, show_id):
        current_user = Users.objects.get(id=request.session['user_id'])
        current_venue = Venues.objects.get(host_id=current_user)
        Shows.objects.get(id=show_id).delete()
        return redirect('/shows/venues/{}'.format(current_venue.id))

def join_show(request, venue_id, show_id):
        current_user = Users.objects.get(id=request.session['user_id'])
        current_venue = Venues.objects.get(id=venue_id)
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

def create_review(request, venue_id):
        current_user = Users.objects.get(id=request.session['user_id'])
        current_venue = Venues.objects.get(id=venue_id)
        review_description = request.POST['review_description']
        rating = request.POST['rating']
        Reviews.objects.create(venue_id=current_venue, user_id=current_user, review_description=review_description, rating=rating )

        return redirect('/shows/venues/{}'.format(venue_id))



def band_submission(request, venue_id, show_id):
        current_user = Users.objects.get(id=request.session['user_id'])
        current_show = Shows.objects.get(id=show_id)
        artist_name = request.POST['artist_name']
        other_profiles = request.POST['other_profiles']
        email = request.POST['email']
        bio = request.POST['bio']
        print current_show
        try:  
                current_band = Musicians.objects.get(user=current_user)
                current_band.artist_name = request.POST['artist_name']
                current_band.other_profiles = request.POST['other_profiles']
                current_band.email = request.POST['email']
                current_band.bio = request.POST['bio']
                current_band.show = current_show
                current_band.save()
        except:
                Musicians.objects.create(show=current_show, user=current_user, artist_name=artist_name, other_profiles=other_profiles, email=email, bio=bio)
        # if current_user.type_of_user == 1:
        #         current_user.type_of_user = 2
        if current_user.type_of_user == 3 or current_user.type_of_user == 4:
                current_user.type_of_user = 4
                current_user.save()
        else:
                current_user.type_of_user = 2
        current_user.save()

        messages.success(request, 'Your submission has been sent!')

        return redirect('/shows/venues/{}'.format(venue_id))

def accept_band(request, venue_id, show_id, musician_id):
        current_band = Musicians.objects.get(id=musician_id)
        current_show = Shows.objects.get(id=show_id)
        current_show.bands = current_show.bands+ ', ' + current_band.artist_name
        current_show.save()
        current_band.delete()
        return redirect('/shows/venues/{}'.format(venue_id))

def deny_band(request, venue_id, musician_id):
        Musicians.objects.get(id=musician_id).delete()
        return redirect('/shows/venues/{}'.format(venue_id))


