from django.shortcuts import render
from django.views.generic import CreateView
from users.forms import SignUpForm


class SignUp(CreateView):
    template_name = 'sign_up.html'
    form_class = SignUpForm
