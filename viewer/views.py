from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, template_name='home.html')

def vehicles(request):
    return render(request, template_name='vehicles.html')

def driving_licenses(request):
    return render(request, template_name='driving_licenses.html')

def login(request):
    return render(request, template_name='login.html')

def register(request):
    return render(request, template_name='register.html')

def about(request):
    return render(request, template_name='about.html')
