from django.urls import path
from users.views import SignUp, UserLoginView


urlpatterns = [
    path('sign-up', SignUp.as_view(), name='sign_up'),
    path('login/', UserLoginView.as_view(), name='login'),
]