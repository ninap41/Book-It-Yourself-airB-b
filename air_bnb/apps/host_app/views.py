# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..host_app.models import Venues
from ..login_app.models import Users

# Create your views here.

        

def add_host(request):
        current_user = Users.objects.get(id=request.session['user_id'])
        single_venue = ''
        try:
                single_venue = Venues.objects.get(host_id=current_user.id)
        except Venues.DoesNotExist:
                single_venue = None
        context= {
                'venues': Venues.objects.all(),
                'user': current_user,
                'venue': single_venue
        }
        current_user = context['user']
        return render(request,'host_app/add_host.html', context, current_user)


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


def create_venue(request):
        current_user = Users.objects.get(id= request.session['user_id'])
        space_name = request.POST['space_name']
        venue_details = request.POST['venue_details']
        dry_zone = request.POST['dry_zone']
        noise_level = request.POST['noise_level']
        capacity= request.POST['capacity']
        photo =  request.FILES['venue_image']
        overnight_option= request.POST['overnight_option']
        suggested_donation= request.POST['suggested_donation']
        promotions= request.POST['promotions']
        gear_availability= request.POST['gear_availability']
        show_start= request.POST['show_start']
        show_end= request.POST['show_end']
        bill_capacity = request.POST['bill_capacity']
        location_type = request.POST['location_type']
        past_performers= request.POST['past_performers']
        street_address = request.POST['street_address']
        city= request.POST['city']
        state= request.POST['state']
        country= request.POST['country']
        zip_code= request.POST['zip_code']
        if current_user.type_of_user == 2 or current_user.type_of_user == 4:
                current_user.type_of_user = 4
        else:
                current_user.type_of_user = 3
        current_user.save()
        
        Venues.objects.create(host_id=current_user, photo=photo, space_name=space_name, venue_details=venue_details,dry_zone=dry_zone,noise_level=noise_level,capacity=capacity, overnight_option=overnight_option, suggested_donation=suggested_donation, promotions=promotions, gear_availability=gear_availability, show_start=show_start, show_end=show_end, bill_capacity=bill_capacity, location_type=location_type, past_performers=past_performers,street_address=street_address, city=city, state=state, country=country, zip_code=zip_code)

        return redirect('/shows')


# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, '/shows', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, '/shows')

