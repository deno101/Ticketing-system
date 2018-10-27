from django.http import HttpResponse
from django.shortcuts import render

# methods that direct urls.py which html file is to which url
def home(request):
    return render(request, 'home.html')


def booking(request):
    return render(request, 'booking.html')


def support(request):
    return render(request, 'support.html')


def help(request):
    return render(request, 'help.html')