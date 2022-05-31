import random

from django.shortcuts import render
from django.http import HttpResponse
from viewer.models import Vehicle, Driving_licenses

# Create your views here.

def home(request):
    return render(request, template_name='home.html')

def vehicles(request):
    return render(request, template_name='vehicles.html')

def driving_licenses(request):
    return render(request, template_name='driving_licenses.html')

def about(request):
    return render(request, template_name='about.html')


def interesting_facts():
    petrol_cars = Vehicle.objects.filter(rodzaj_paliwa='BENZYNA').count()
    rope_cars = Vehicle.objects.filter(rodzaj_paliwa='OLEJ NAPĘDOWY').count()
    gas_cars = Vehicle.objects.filter(rodzaj_paliwa__contains='GAZ').count()
    voivodeships = ['DOLNOŚLĄSKIE', 'KUJAWSKO-POMORSKIE', 'LUBELSKIE', 'ŁÓDZKIE', 'MAŁOPOLSKIE', 'MAZOWIECKIE', 'OPOLSKIE', 'PODKARPACKIE', 'PODLASKIE', 'POMORSKIE', 'ŚLĄSKIE', 'ŚWIĘTOKRZYSKIE', 'WARMIŃSKO-MAZURSKIE', 'WIELKOPOLSKIE', 'ZACHODNIOPOMORSKIE']
    random_voivodeship = random.choice(voivodeships)
    # for voivodeship in voivodeships:
    #     result = Vehicle.objects.filter(wojewodztwo=voivodeship).count()
    #     print(f"Liczba zarejestrowanych pojazdów, województwo {voivodeship.title()}: {result}.")
    number_all_cars = Vehicle.objects.filter(wojewodztwo=random_voivodeship).count()
    number_one_mar_cars = Vehicle.objects.filter(wojewodztwo=random_voivodeship, marka='TOYOTA').count()
    math_result = number_one_mar_cars*100/number_all_cars
    print(f"{round(math_result,2)}% aut województwa {random_voivodeship.title()} to Toyoty.")
    print(f"Ilość zarejestrowanych pojazdów na paliwo: {petrol_cars}, rope: {rope_cars}, gaz: {gas_cars}.")
