from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    # return HttpResponse("Hi! You're in my Home")
    return render(request, 'generator/home.html', {'password':'asjgjhasvkbj'})

def password(request):
    # return HttpResponse("Eggs are awsome and it is tasty!")
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))

    length = int(request.GET.get('passLength'))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
