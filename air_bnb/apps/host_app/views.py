# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..host_app.models import Venues
from ..login_app.models import Users

# Create your views here.
def add_host(request):
        context= {
                'venues': Venues.objects.all()
        }
        return render(request,'host_app/add_host.html', context)

def create_venue(request):
        current_user = Users.objects.get(id= request.session['user_id'])
        space_name = request.POST['space_name']
        venue_details = request.POST['venue_details']
        dry_zone = request.POST['dry_zone']
        noise_level = request.POST['noise_level']
        capacity= request.POST['capacity']
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
        
        Venues.objects.create(host_id=current_user,space_name=space_name, venue_details=venue_details,dry_zone=dry_zone,noise_level=noise_level,capacity=capacity, overnight_option=overnight_option, suggested_donation=suggested_donation, promotions=promotions, gear_availability=gear_availability, show_start=show_start, show_end=show_end, bill_capacity=bill_capacity, location_type=location_type, past_performers=past_performers,street_address=street_address, city=city, state=state, country=country, zip_code=zip_code)

        

        
        return redirect('/shows')


