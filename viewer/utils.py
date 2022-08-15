"""
Hi! You are in back-end side of 'cepik_app. So, if you are a 'Front-end Team' - run away! ;)
There are three funcs. 'Download_vehicles', 'Download_licences', and 'download_data' to
automatic both. Running in shell.
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
import urllib.request
from viewer.models import Vehicle, Driving_licenses, Voivodeship


def download_data():
    """
    download data from API for all voivodeships.
    """
    start = time.time()
    voivodeships = ['02', '04', '06', '08', '10', '12', '14', '16', '18', '20',
                    '22', '24', '26', '28', '30', '32']  # list of voivodeships. Explanation in
    # docstring.
    choose = input('type 1(vehicles) or 2(driving_licenses): ')
    if choose == '1':
        for voivo in voivodeships:
            # try:
                url = f'https://api.cepik.gov.pl/pojazdy?wojewodztwo={voivo}&data-od=20220301' \
                      f'&data-do=20220331&pokaz-wszystkie-pola=true'
                print(f'voivodeship {voivo}')
                download_vehicles(url)
            # except (IndexError, KeyError, TimeoutError):
            #     continue
        end = time.time()
        seconds = round(end - start)
        print('All done!')
        print(f'it has taken {seconds} seconds.')

    elif choose == '2':
        for voivo in voivodeships:
            for page in range(1, 219):
                try:
                    url = f'https://api.cepik.gov.pl/prawa-jazdy?filter[wojewodztwo-kod]={voivo}' \
                          f'&page={page}'
                    print(f'voivodeship {voivo}')
                    print(f'page {page}')
                    download_licences(url)
                except (IndexError, KeyError):
                    continue
    else:
        print('wrong input')
    end = time.time()
    seconds = round(end - start)
    print(f'it has taken {seconds} seconds.')


def download_vehicles(url):
    """
    Func send request to API and turn response into json.
    Next transforms selected data from json to local database.
    """
    requests.packages.urllib3.disable_warnings()  # type:ignore
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'  # type:ignore
    response = requests.get(url)
    vehicles = response.json()
    # if vehicles['meta']['page'] < 2:
    all_vehs = vehicles['meta']['count']
    print(all_vehs)
    # count = 0

    if vehicles['data']:
        in_case_of_error = vehicles['links']['self']
        vehicles_to_db = vehicles['data']
        # if vehicles['meta']['page'] == 1:
        # all_vehs = vehicles['meta']['count']
        # print(f'Still {all_vehs-count} to download...')

        # count = 0
        for vehicle in vehicles_to_db:

            vehicle_in_database = Vehicle.objects.filter(id_cepik=vehicle['id']).exists()  # type: ignore
            if not vehicle_in_database:
                vehs = Vehicle(id_cepik=vehicle['id'],
                               id_wojewodztwa=vehicle['attributes']['wojewodztwo-kod'],
                               # wojewodztwo=vehicle['attributes']['rejestracja-wojewodztwo'],
                               marka=vehicle['attributes']['marka'],
                               model=vehicle['attributes']['model'],
                               rodzaj_pojazdu=vehicle['attributes']['rodzaj-pojazdu'],
                               pochodzenie_pojazdu=vehicle['attributes']['pochodzenie-pojazdu'],
                               rok_produkcji=vehicle['attributes']['rok-produkcji'],
                               pojemnosc_skokowa=vehicle['attributes']['pojemnosc-skokowa-silnika'],
                               dmc=vehicle['attributes']['dopuszczalna-masa-calkowita'],
                               liczba_miejsc=vehicle['attributes']['liczba-miejsc-ogolem'],
                               rodzaj_paliwa=vehicle['attributes']['rodzaj-paliwa'],
                               hak=vehicle['attributes']['hak'],
                               kierownica_po_prawej=vehicle['attributes']
                               ['kierownica-po-prawej-stronie'],
                               data_ostatniej_rejestracji_w_kraju=vehicle['attributes']
                               ['data-ostatniej-rejestracji-w-kraju'])
                voivo = Voivodeship(wojewodztwo=vehicle['attributes']['rejestracja-wojewodztwo'])
                vehs.save()
                voivo.save()
                # count += 1
                # print(f'{count} done...')

        try:
            next_page = vehicles['links']['next']
            download_vehicles(next_page)
        except KeyError:
            print('all done...')
        except (TimeoutError, ConnectionError):
            download_vehicles(in_case_of_error)
        except:
            time.sleep(20)
            download_vehicles(in_case_of_error)


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
