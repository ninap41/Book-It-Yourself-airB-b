# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from models import Users
# Create your views here.

def index(request):
    return render(request, 'login_app/index.html')

def registration(request):
    errors = Users.objects.registration_validation(request.POST)
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    birthday = request.POST['birthday']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    password = request.POST['password']
    if len(errors):
        for error in errors:
            messages.warning(request, error)
        return redirect('/')
    else:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt(12))
        Users.objects.create(first_name=first_name, last_name=last_name, email=email, birthday=birthday, password=hashed_password, phone_number=phone_number, type_of_user=1)
        user_login = Users.objects.get(first_name=first_name, last_name=last_name, email=email, birthday=birthday)
        user_login_id = user_login.id
        request.session['name'] = first_name
        request.session['user_id'] = user_login_id
        return redirect('/homepage')


def login(request):
    errors = Users.objects.login_validation(request.POST)
    password = request.POST['password']
    try:
        user_login = Users.objects.get(email=request.POST['email'])
    except Exception:
        errors.append('Email not in our database')
        for error in errors:
            messages.warning(request, error)
        return redirect('/')

    password_check = bcrypt.checkpw(password.encode(), user_login.password.encode())

    if password_check == True:
        request.session['name'] = user_login.first_name
        request.session['user_id'] = user_login.id
        return redirect('/homepage')
    else:
        errors.append('Email/Password is incorrect')
        for error in errors:
            messages.warning(request, error)
        return redirect('/')

def update_user(request):
    current_user = Users.objects.get(id=request.session['user_id'])
    # Eventually add Venues.objects.get(host_id=current_user) and Musicians.objects.get(musician_id=current_user) to the context
    context = {
        'user': current_user
    }
    return render(request, 'login_app/update_user.html', context)

def logout(request):
    request.session['name'] = ''
    return redirect('/')

def homepage(request):
    return render(request, "login_app/homepage.html")

# $2b$12$nmLxzfTq2Ixi7Hi39hpG.unJPRxdcnvWw57KAZOJbTWAnulB17ZCe