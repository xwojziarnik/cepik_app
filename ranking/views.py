from django.shortcuts import render

from viewer.models import Vehicle


def pie_stat(request):
    context = dict()
    context['benzyna'] = Vehicle.objects.filter(rodzaj_paliwa='BENZYNA').count()  # type:ignore
    context['olej'] = Vehicle.objects.filter(rodzaj_paliwa='OLEJ NAPĘDOWY').count()  # type:ignore
    context['elektryka'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA').count()  # type:ignore
    context['inne'] = Vehicle.objects.exclude(rodzaj_paliwa='BENZYNA')\
                                     .exclude(rodzaj_paliwa='OLEJ NAPĘDOWY')\
                                     .exclude(rodzaj_paliwa='ENERGIA ELEKTRYCZNA').count()
    return render(request, 'pie_chart.html', context)


def rank(request):
    context = dict()
    # context['dolnoslaskie'] = (Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')
    #                            .filter(id_wojewodztwa='02').count()) * 100 /\
    #                           (Vehicle.objects.filter(id_wojewodztwa='02').count())
    # context['kujawsko_pomorskie'] = (Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')
    #                                  .filter(id_wojewodztwa='04').count()) * 100 /\
    #                                 (Vehicle.objects.filter(id_wojewodztwa='04').count())
    # context['lubelskie'] = (Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')
    #                         .filter(id_wojewodztwa='06').count()) * 100 /\
    #                        (Vehicle.objects.filter(id_wojewodztwa='06').count())
    context['dolnoslaskie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='02').count()
    context['kujawsko_pomorskie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='04').count()
    context['lubelskie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='06').count()
    context['lubuskie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='08').count()
    context['lodzkie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='10').count()
    context['malopolskie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='12').count()
    context['mazowieckie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='14').count()
    context['opolskie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='16').count()
    context['podkarackie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='18').count()
    context['podlaskie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='20').count()
    context['pomorskie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='22').count()
    context['slaskie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='24').count()
    context['swietokrzyskie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='26').count()
    context['warm_mazurskie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='28').count()
    context['wielkopolskie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='30').count()
    context['zachodniopomorskie'] = Vehicle.objects.filter(rodzaj_paliwa='ENERGIA ELEKTRYCZNA')\
        .filter(id_wojewodztwa='32').count()

    return render(request, 'chart.html', context)
