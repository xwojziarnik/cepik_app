from django.contrib.auth.forms import UserCreationForm
from django import forms
# from models import MyModel
# from django.db import models


class SignUpForm(UserCreationForm):
    voivodeship = forms.CharField()
    pass
    #voivodeship = models.CharField(choices=MyModel.Voivodeship.choices)

