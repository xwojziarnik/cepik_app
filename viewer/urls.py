from django.urls import path
from . import views
from users import views as u
from viewer import crud

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicles/', views.vehicles),
    path('driving-licenses/', views.driving_licenses),
    path('about/', views.about),
    path('sign-up/', u.SignUp.as_view(), name='sign_up'),
    path('login-user/', u.login_user, name='loginAuth'),
    path('logout-user', u.logout_user, name='user_logout'),
    path('create/', crud.vehicle_create_view, name='create_vehicle'),
    path('list-view/', crud.VehicleListView.as_view(), name='vehicle_list_view'),
    path('list-view/<id>', crud.vehicle_detail_view, name='detail_view_vehicle'),
    path('<id>/update', crud.vehicle_update_view, name='update_view_vehicle'),
    path('<id>/delete', crud.vehicle_delete_view, name='delete_view_vehicle'),

]