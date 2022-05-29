from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import SignUpForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class SignUp(CreateView):
    template_name = 'registration/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('loginAuth')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Zalogowano pomyślnie.")
            return redirect('home')
        else:
            messages.success(request, "Błędny login i/lub hasło")
            return redirect('loginAuth')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Wylogowano pomyślnie.")
    return redirect('loginAuth')
