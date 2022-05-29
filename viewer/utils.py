"""
Hi! You are in back-end side of 'cepik_app. So, if you are a 'Front-end Team' - run away! ;)
There are three funcs. 'Download_vehicles', 'Download_licences', and 'download_data' to
automatic both. Running is shell.
Voivodeships:
02 dolnośląskie
04 kujawsko-pomorskie
06 lubelskie
08 lubuskie
10 łódzkie
12 małopolskie
14 mazowieckie
16 opolskie
18 podkarpackie
20 podlaskie
22 pomorskie
24 śląskie
26 świętokrzyskie
28 warm-mazurskie
30 wielkpolskie
32 zachodniopomorskie
"""

import time
import requests
from viewer.models import Vehicle, Driving_licenses


def download_data():
    """
    download data from API for all voivodeships.
    """
    voivodeships = ['02', '04', '06', '08', '10', '12', '14', '16', '18', '20', '22',
                    '24', '26', '28', '30', '32']  # list of voivodeships. Explanation in docstring.
    choose = input('type 1(vehicles) or 2(driving_licenses): ')
    if choose == '1':
        for voivo in voivodeships:
            for page in range(1, 11):   # API limits - 100 calling/ one minute
                if page % 2 == 0:       # 100 result per page
                    print('hold')       # next page needs to wait 60 seconds
                    time.sleep(60)
                try:
                    url = f'https://api.cepik.gov.pl/pojazdy?wojewodztwo={voivo}&data-od=20220403&page={page}'
                    print(f'voivodeship {voivo}')
                    print(f'page {page}')
                    download_vehicles(url)
                except IndexError:
                    break

    elif choose == '2':
        for voivo in voivodeships:
            for page in range(1, 11):
                try:
                    url = f'https://api.cepik.gov.pl/prawa-jazdy?filter[wojewodztwo-kod]={voivo}&page={page}'
                    print(voivo)
                    download_licences(url)
                except IndexError:
                    break
    else:
        print('wrong input')


def download_vehicles(url):
    """
    Func send request to API and turn response into json.
    Next transforms selected data from json to local database.
    """
    requests.packages.urllib3.disable_warnings()  # type:ignore
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'  # type:ignore
    response = requests.get(url)
    vehicles = response.json()
    if vehicles['data']:
        vehicles = vehicles['data']
        count = 0
        for veh in vehicles:
            requests.packages.urllib3.disable_warnings()  # type:ignore
            requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'  # type:ignore
            url = veh['links']['self']
            response = requests.get(url)
            vehicle = response.json()

            vehicle = vehicle['data']

            vehicle_in_database = Vehicle.objects.filter(id_cepik=vehicle['id']).exists()  # type: ignore
            if not vehicle_in_database:
                vehs = Vehicle(id_cepik=vehicle['id'], id_wojewodztwa=vehicle['attributes']['wojewodztwo-kod'],
                               wojewodztwo=vehicle['attributes']['rejestracja-wojewodztwo'],
                               marka=vehicle['attributes']['marka'], model=vehicle['attributes']['model'],
                               rodzaj_pojazdu=vehicle['attributes']['rodzaj-pojazdu'],
                               pochodzenie_pojazdu=vehicle['attributes']['pochodzenie-pojazdu'],
                               rok_produkcji=vehicle['attributes']['rok-produkcji'],
                               pojemnosc_skokowa=vehicle['attributes']['pojemnosc-skokowa-silnika'],
                               dmc=vehicle['attributes']['dopuszczalna-masa-calkowita'],
                               liczba_miejsc=vehicle['attributes']['liczba-miejsc-ogolem'],
                               rodzaj_paliwa=vehicle['attributes']['rodzaj-paliwa'],
                               hak=vehicle['attributes']['hak'],
                               kierownica_po_prawej=vehicle['attributes']['kierownica-po-prawej-stronie'])
                vehs.save()
                count += 1
                print('done - ', count)


def download_licences(url):
    """
    Func send request to API and turn response into json.
    Next transforms selected data from json to local database.
    """
    requests.packages.urllib3.disable_warnings()  # type:ignore
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'  # type:ignore
    response = requests.get(url)
    licenses = response.json()
    licenses = licenses['data'][0]
    licenses_in_database = Driving_licenses.objects.filter(id_cepik=licenses['id']).exists()  # type: ignore
    count = 0
    if not licenses_in_database:
        licens = Driving_licenses(id_cepik=licenses['id'],
                                  data_uprawnien=licenses['attributes']['data-statystyki'],
                                  id_wojewodztwa=licenses['attributes']['wojewodztwo-kod'],
                                  wojewodztwo=licenses['attributes']['wojewodztwo-nazwa'],
                                  plec=licenses['attributes']['plec'],
                                  wiek=licenses['attributes']['wiek'],
                                  ilosc=licenses['attributes']['ilosc'])

        licens.save()
        count += 1
        print('done - ', count)

