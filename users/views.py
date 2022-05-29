from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from users.forms import SignUpForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class SignUp(CreateView):
    template_name = 'sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'authenticate/login.html'
    success_url = reverse_lazy('index')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Success Login.")
            return redirect('index')
        else:
            messages.success(request, "Error Logging in, try again...")
            return redirect('loginAuth')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out.")
    return redirect('loginAuth')


class AppListView(ListView):
    template_name = 'index.html'
