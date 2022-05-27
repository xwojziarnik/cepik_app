from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from users.forms import SignUpForm


class SignUp(CreateView):
    template_name = 'sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')


class AppListView(ListView):
    template_name = 'index.html'
