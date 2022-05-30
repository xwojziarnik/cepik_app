from django.db import models


class Voivodeship(models.Model):
    wojewodztwo = models.CharField(max_length=45, null=True)
    id_wojewodztwa = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.wojewodztwo


class Vehicle(models.Model):
    d = models.ManyToManyField
    id_cepik = models.IntegerField(default=0)
    marka = models.CharField(max_length=45, null=True)
    model = models.CharField(max_length=45, null=True)
    id_wojewodztwa = models.IntegerField(default=0, null=False)
    wojewodztwo = models.CharField(max_length=45, null=True)
    rodzaj_pojazdu = models.CharField(max_length=45, null=True)
    pochodzenie_pojazdu = models.CharField(max_length=45, null=True)
    rok_produkcji = models.CharField(max_length=45, null=True)
    pojemnosc_skokowa = models.DecimalField(decimal_places=1, max_digits=20, default=1, null=True)
    dmc = models.CharField(max_length=45, null=True)
    liczba_miejsc = models.IntegerField(default=1, null=True)
    rodzaj_paliwa = models.CharField(max_length=45, null=True)
    hak = models.BooleanField(default=False)
    kierownica_po_prawej = models.BooleanField(null=True)

    def __str__(self):
        return f'{self.marka}-{self.model}-{self.rok_produkcji}-{self.rodzaj_paliwa}.'


class Driving_licenses(models.Model):
    id_cepik = models.CharField(max_length=45, null=False)
    data_uprawnien = models.CharField(max_length=45, null=False)
    id_wojewodztwa = models.IntegerField(default=0, null=False)
    wojewodztwo = models.CharField(max_length=45, null=True)
    plec = models.CharField(max_length=12, null=True)
    wiek = models.IntegerField(default=1, null=True)
    ilosc = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f'{self.data_uprawnien}-{self.wojewodztwo}-{self.plec}-{self.wiek}-{self.ilosc}.'