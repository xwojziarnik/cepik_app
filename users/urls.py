from django.urls import path
from users.views import SignUp


urlpatterns = [
    path('sign-up', SignUp.as_view(), name='sign_up'),
]