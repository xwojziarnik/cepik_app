from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('vehicles', views.vehicles),
    path('driving-licenses', views.driving_licenses),
    path('login', views.login),
    path('register/', views.register),
    path('about', views.about),
]