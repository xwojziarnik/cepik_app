from django.urls import path
from ranking import views


urlpatterns = [
    path('ranking', views.rank, name='home'),
    path('pie', views.pie_stat, name='pie')
]
