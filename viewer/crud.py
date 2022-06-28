from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.forms import ModelForm
from django import forms
from django.urls import reverse_lazy
from django.views.generic import ListView
from viewer.models import Vehicle


class VehicleForm(ModelForm):
    choice = (('1', 'DOLNOŚLĄSKIE'), ('2', 'KUJAWSKO-POMORSKIE'), ('3', 'LUBELSKIE'), ('4', 'LUBUSKIE'),
              ('5', 'ŁÓDZKIE'), ('6', 'MAŁOPOLSKIE'), ('7', 'MAZOWIECKIE'), ('8', 'OPOLSKIE'), ('9', 'PODKARPACKIE'),
              ('10', 'PODLASKIE'), ('11', 'POMORSKIE'), ('12', 'ŚLĄSKIE'), ('13', 'ŚWIĘTOKRZYSKIE'),
              ('14', 'WARMIŃSKO-MAZURSKIE'), ('15', 'WIELKOPOLSKIE'), ('16', 'ZACHODNIOPOMORSKIE'))
    wojewodztwo = forms.ChoiceField(choices=choice)

    class Meta:
        model = Vehicle
        fields = [
            'marka',
            'model',
            'wojewodztwo',
            'rodzaj_pojazdu',
            'pochodzenie_pojazdu',
            'rok_produkcji',
            'pojemnosc_skokowa',
            'dmc',
            'liczba_miejsc',
            'rodzaj_paliwa',
            'hak',
            'kierownica_po_prawej'
        ]


def vehicle_create_view(request):

    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    success_url = reverse_lazy('CreateVehicle')

    return render(request, 'vehicle_create_view.html', context)


class VehicleListView(ListView):
    template_name = 'vehicles_list_view.html'
    model = Vehicle
    paginate_by = 10


def vehicle_detail_view(request, id):
    context = dict()
    context['data'] = Vehicle.objects.get(id=id)    # type: ignore
    return render(request, 'vehicle_detail_view.html', context)


def vehicle_update_view(request, id):
    context = dict()
    obj = get_object_or_404(Vehicle, id=id)
    form = VehicleForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/vehicles/')
    context['form'] = form

    return render(request, 'vehicle_update_view.html', context)


def vehicle_delete_view(request, id):
    context = dict()
    context['data'] = Vehicle.objects.get(id=id)    # type: ignore
    obj = get_object_or_404(Vehicle, id=id)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('/vehicles/')

    return render(request, 'vehicle_delete_view.html', context)
