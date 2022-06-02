from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
# from logging import getLogger
from django.forms import (
  CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea, ModelForm
)
from django.urls import reverse_lazy
from django.views.generic import CreateView
from viewer.models import Vehicle, Driving_licenses

# LOGGER = getLogger()


class VehicleForm(ModelForm):
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

    # def form_invalid(self, form):
        # LOGGER.warning('User provided invalid data.')
        # return super().form_invalid(form)
    return render(request, 'vehicle_create_view.html', context)


def vehicle_list_view(request):
    context = {}
    context['dataset'] = Vehicle.objects.all()

    return render(request, 'vehicles_list_view.html', context)


def vehicle_detail_view(request, id):
    context = {}
    context['data'] = Vehicle.objects.get(id=id)
    return render(request, 'vehicle_detail_view.html', context)


def vehicle_update_view(request, id):
    context = {}

    obj = get_object_or_404(Vehicle, id=id)

    form = VehicleForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/'+id)

    context['form'] = form

    return render(request, 'vehicle_update_view.html', context)


def vehicle_delete_view(request, id):
    context = {}
    context['data'] = Vehicle.objects.get(id=id)
    obj = get_object_or_404(Vehicle, id=id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('/')

    return render(request, 'vehicle_delete_view.html', context)
