from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings

import random
from .models import RestaurantAdmin, Restaurant
from user_app import models as user_models



def register_admin(data:dict, restaurant:Restaurant):
    email:str = data.get('name').replace(' ','').lower()+'@bhoklagyo.com'
    phone:str = data.get('phone')
    passkey_raw:str = str(data.get('name').replace(' ',''))+str(phone)
    random_pass:str = ''.join(random.choices(passkey_raw,k=10))
    user:user_models.User = user_models.User.objects.create(
        email = email,
        phone = phone,
        password = make_password(random_pass),
        is_staff = True,
        role = user_models.User.RESTAURANT_ADMIN,
    )
    admin:RestaurantAdmin = RestaurantAdmin(
        user = user,
        restaurant_name=restaurant,
    )
    
    send_mail(
        'Your password for Bhoklagyo',
        f'Your password for Bhoklagyo with email {email} is <b>{random_pass}.\
        Make sure you do not share it with anybody.',
        f'{settings.EMAIL_HOST_USER}',
        [f'bhattarais009@gmail.com'],
        fail_silently=False,
    )
    
def register_restaurant_form(request):
    if request.method == 'POST':
        name = request.POST.get('restaurant_name','')
        location = request.POST.get('address','')
        phone = request.POST.get('phone','')
        pan = request.POST.get('pan','')
        # email = request.POST.get('email')
        data ={
            'name':name,
            'location':location,
            'phone':phone,
            'PAN':pan
        }
        
        restaurant = register_restaurant(data)
        register_admin(data, restaurant)
        return redirect('login-restaurant')
    return render(request, 'restaurant_app/register.html')

def register_restaurant(data):        
    restaurant = Restaurant.objects.create(
        restaurant_name = data.get('name'),
        location = data.get('location'),
        phone = data.get('phone'),
        )

    restaurant.save()
    return restaurant

def login_admin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email: {email} Password: {password} ")
        admin = authenticate(request, email=email, password=password, role=user_models.User.RESTAURANT_ADMIN)
        
        if admin:
            login(request, admin)
            return HttpResponse(f"Success path <strong>{admin}</strong>  authenticated : <strong>{admin.is_authenticated}</strong>")
        else:
            message = messages.error(request, "Unable to login. Please input valid credentials.")
            return render(request, 'restaurant_app/login-admin.html',{'message':message})
    else:
        return render(request, 'restaurant_app/login-admin.html')
    
    
def logout_admin(request):
    logout(request)
    return redirect('login')

def add_food(request):
    user = user_models.User.objects.get(id=request.user.id)

    if user:
        return HttpResponse('This user can add food in menu')
    
    else:
        return HttpResponse('You are not authorised to view this page.')

# modified by shantosh upload by ashant for restaurant admin panel
def restro_admin(request):
    return render(request, 'restaurant_app/admin-panel.html')
