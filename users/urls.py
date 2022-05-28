from django.urls import path

from users import views
from users.views import SignUp, UserLoginView, AppListView

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign_up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('login_user/', views.login_user, name='loginAuth'),
    path('logout_user/', views.logout_user, name='logout'),
    path('', AppListView.as_view(), name='index'),
]