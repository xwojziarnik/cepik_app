from django.urls import path
from . import views
from users import views as u

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicles/', views.vehicles),
    path('driving-licenses/', views.driving_licenses),
    path('about/', views.about),
    path('sign-up/', u.SignUp.as_view(), name='sign_up'),
    path('login-user/', u.login_user, name='loginAuth'),
    path('logout-user', u.logout_user, name='user_logout'),

]