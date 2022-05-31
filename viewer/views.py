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
    cars = ['TOYOTA', 'VOLKSWAGEN', 'HYUNDAI', 'BMW', 'AUDI', 'RENAULT', 'HONDA', 'KIA', 'FIAT', 'MAZDA', 'OPEL', 'VOLVO', 'FORD', 'SKODA', 'SUBARU', 'MERCEDES-BENZ']
    random_car = random.choice(cars)
    # for voivodeship in voivodeships:
    #     result = Vehicle.objects.filter(wojewodztwo=voivodeship).count()
    #     print(f"Liczba zarejestrowanych pojazdów, województwo {voivodeship.title()}: {result}.")
    number_all_cars = Vehicle.objects.filter(wojewodztwo=random_voivodeship).count()
    number_one_mark_cars = Vehicle.objects.filter(wojewodztwo=random_voivodeship, marka=random_car).count()
    math_result_car = number_one_mark_cars*100/number_all_cars
    print(f"{random_voivodeship.title()} to województwo w którym {round(math_result_car,2)}% aut to {random_car.title()}.")
    print(f"Ilość zarejestrowanych pojazdów na benzynę: {petrol_cars} szt., na ropę: {rope_cars} szt., gaz: {gas_cars} szt.")
    number_f_drivers_voivodeship = Driving_licenses.objects.filter(plec='K', wojewodztwo=random_voivodeship).count()
    number_m_drivers_voivodeship = Driving_licenses.objects.filter(plec='M', wojewodztwo=random_voivodeship).count()
    math_result_sex_f = number_f_drivers_voivodeship*100/(number_f_drivers_voivodeship+number_m_drivers_voivodeship)
    math_result_sex_m = number_m_drivers_voivodeship*100/(number_f_drivers_voivodeship+number_m_drivers_voivodeship)
    print(f"Kobiety stanowią {round(math_result_sex_f, 2)}% kierowców województwa {random_voivodeship.title()}go.")
    print(f"Mężczyźni stanowią {round(math_result_sex_m, 2)}% kierowców województwa {random_voivodeship.title()}go.")
    age_under_f = Driving_licenses.objects.filter(plec='K', wiek__lt=40).count()
    age_under_m = Driving_licenses.objects.filter(plec='M', wiek__lt=40).count()
    age_over_f = Driving_licenses.objects.filter(plec='M', wiek__gte=40).count()
    age_over_m = Driving_licenses.objects.filter(plec='M', wiek__gte=40).count()
    number_f_drivers = Driving_licenses.objects.filter(plec='K').count()
    number_m_drivers = Driving_licenses.objects.filter(plec='M').count()
    math_result_age_under_f = age_under_f*100/number_f_drivers
    math_result_age_under_m = age_under_m*100/number_m_drivers
    math_result_age_over_f = age_over_f*100/number_f_drivers
    math_result_age_over_m = age_over_m*100/number_m_drivers
    print(f"Kobiety poniżej 40 roku życia stanowią {round(math_result_age_under_f, 2)}% kierowców.")
    print(f"Mężczyźni poniżej 40 roku życia stanowią {round(math_result_age_under_m, 2)}% kierowców.")
    print(f"Kobiety w wieku 40 lat i więcej stanowią {round(math_result_age_over_f, 2)}% kierowców.")
    print(f"Mężczyźni w wieku 40 lat i więcej stanowią {round(math_result_age_over_m, 2)}% kierowców.")