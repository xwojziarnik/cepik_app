import random

from django.contrib import messages
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from viewer.models import Vehicle, Driving_licenses

# Create your views here.

def home(request):
    messages.success(request, interesting_facts())
    return render(request, template_name='home.html')

def vehicles(request):
    return render(request, template_name='vehicles.html')

def driving_licenses(request):
    return render(request, template_name='driving_licenses.html')

def about(request):
    return render(request, template_name='about.html')

def team(request):
    return render(request, template_name='team.html')

def interesting_facts():
    """
    The function was responsible for displaying random facts extracted from the database.
    """
    petrol_cars = Vehicle.objects.filter(rodzaj_paliwa='BENZYNA').count()
    rope_cars = Vehicle.objects.filter(rodzaj_paliwa='OLEJ NAPĘDOWY').count()
    gas_cars = Vehicle.objects.filter(rodzaj_paliwa__contains='GAZ').count()
    random_voivodeship = random.choice(['DOLNOŚLĄSKIE', 'KUJAWSKO-POMORSKIE', 'LUBELSKIE', 'ŁÓDZKIE', 'MAŁOPOLSKIE',
                                        'MAZOWIECKIE', 'OPOLSKIE', 'PODKARPACKIE', 'PODLASKIE', 'POMORSKIE', 'ŚLĄSKIE',
                                        'ŚWIĘTOKRZYSKIE', 'WARMIŃSKO-MAZURSKIE', 'WIELKOPOLSKIE', 'ZACHODNIOPOMORSKIE'])
    random_car = random.choice(['TOYOTA', 'VOLKSWAGEN', 'HYUNDAI', 'BMW', 'AUDI', 'RENAULT', 'HONDA', 'KIA', 'FIAT',
                                'MAZDA', 'OPEL', 'VOLVO', 'FORD', 'SKODA', 'SUBARU', 'MERCEDES-BENZ'])
    number_all_cars = Vehicle.objects.filter(wojewodztwo=random_voivodeship).count()
    number_one_mark_cars = Vehicle.objects.filter(wojewodztwo=random_voivodeship, marka=random_car).count()
    math_result_car = number_one_mark_cars*100/number_all_cars
    fact_one = f"{random_voivodeship.title()} to województwo w którym " \
               f"{round(math_result_car,2)}% aut to {random_car.title()}."
    fact_two = f"Ilość zarejestrowanych pojazdów na benzynę: {petrol_cars} szt., na ropę: {rope_cars} szt.," \
               f" gaz: {gas_cars} szt."
    number_f_drivers_voivodeship = Driving_licenses.objects.filter(plec='K', wojewodztwo=random_voivodeship).count()
    number_m_drivers_voivodeship = Driving_licenses.objects.filter(plec='M', wojewodztwo=random_voivodeship).count()
    math_result_sex_f = number_f_drivers_voivodeship*100/(number_f_drivers_voivodeship+number_m_drivers_voivodeship)
    math_result_sex_m = number_m_drivers_voivodeship*100/(number_f_drivers_voivodeship+number_m_drivers_voivodeship)
    fact_three = (f"Kobiety stanowią {round(math_result_sex_f, 2)}% kierowców"
                  f" województwa {random_voivodeship.title()}go.")
    fact_four = (f"Mężczyźni stanowią {round(math_result_sex_m, 2)}% kierowców"
                 f" województwa {random_voivodeship.title()}go.")
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
    fact_five = f"Kobiety poniżej 40 roku życia stanowią {round(math_result_age_under_f, 2)}% kierowców."
    fact_six = f"Mężczyźni poniżej 40 roku życia stanowią {round(math_result_age_under_m, 2)}% kierowców."
    fact_seven = f"Kobiety w wieku 40 lat i więcej stanowią {round(math_result_age_over_f, 2)}% kierowców."
    fact_eight = f"Mężczyźni w wieku 40 lat i więcej stanowią {round(math_result_age_over_m, 2)}% kierowców."
    return random.choice([fact_one, fact_two, fact_three, fact_four, fact_five, fact_six, fact_seven, fact_eight])

class DrivingLicenses(ModelForm):
    class Meta:
        model = Driving_licenses
        fields = [
            'data_uprawnien',
            'id_wojewodztwa',
            'wojewodztwo',
            'plec',
            'wiek',
            'ilosc',
        ]


class DrivingLicensesListView(ListView):
    template_name = 'driving_licenses.html'
    model = Driving_licenses
    paginate_by = 10
    ordering = 'id_wojewodztwa', 'data_uprawnien'

