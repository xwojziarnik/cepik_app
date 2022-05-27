from django.contrib.auth.forms import UserCreationForm
from django import forms


VOIVODESHIPS_CHOICES = (
    ("1", "Zachodnio - Pomorskie"),
    ("2", "Pomorskie"),
    ("3", "Warmińsko - Mazurskie"),
    ("4", "Lubuskie"),
    ("5", "Kujawsko - Pomorskie"),
    ("6", "Mazowieckie"),
    ("7", "Podlaskie"),
    ("8", "Dolnośląskie"),
    ("9", "Łódźkie"),
    ("10", "Lubelskie"),
    ("11", "Opolskie"),
    ("12", "Śląskie"),
    ("13", "Świętokrzyskie"),
    ("14", "Małopolskie"),
    ("15", "Podkarpackie"),
    ("15", "Podkarpackie"),
    ("16", "Wielkopolskie"),
)


class SignUpForm(UserCreationForm, forms.Form):
    voivodeship_field = forms.ChoiceField(choices=VOIVODESHIPS_CHOICES)


