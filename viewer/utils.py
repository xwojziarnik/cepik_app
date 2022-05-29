from django.shortcuts import render
import requests
from viewer.models import Vehicle, Driving_licenses
import time


def all_voivodeships():
    voivo = ['08', '10', '12', '14', '16''18', '20', '22',
             '24', '26', '28', '30', '32']
    vdl = input('type 1(vehicles) or 2(driving_licenses): ')
    if vdl == '1':
        for num in voivo:
            for page in range(1, 11):
                if page % 2 == 0:
                    print('hold')
                    time.sleep(60)
                try:
                    url = f'https://api.cepik.gov.pl/pojazdy?wojewodztwo={num}&data-od=20220501&page={page}'
                    print(f'voivodeship {num}')
                    print(f'page {page}')
                    api_to_db(url)
                except IndexError:
                    break

    elif vdl == '2':
        for num in voivo:
            for page in range(1, 11):
                try:
                    url = f'https://api.cepik.gov.pl/prawa-jazdy?filter[wojewodztwo-kod]={num}&page={page}'
                    print(num)
                    api_to_db_licences(url)
                except IndexError:
                    break
    else:
        print('wrong input')


def api_to_db(url):
    requests.packages.urllib3.disable_warnings()  # type:ignore
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'  # type:ignore
    response = requests.get(url)
    vehicles = response.json()
    if vehicles['data']:
        vehicles = vehicles['data']
        count = 0
        for i in vehicles:
            requests.packages.urllib3.disable_warnings()  # type:ignore
            requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'  # type:ignore
            url = i['links']['self']
            response = requests.get(url)
            vehicle = response.json()

            vehicle = vehicle['data']

            vehicle_in_database = Vehicle.objects.filter(id_cepik=vehicle['id']).exists()
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


def api_to_db_licences(url):
    requests.packages.urllib3.disable_warnings()  # type:ignore
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'  # type:ignore
    response = requests.get(url)
    licenses = response.json()
    licenses = licenses['data'][0]
    licenses_in_database = Driving_licenses.objects.filter(id_cepik=licenses['id']).exists()
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
    ...
