from django.contrib import admin
from django.urls import path

from viewer.models import Vehicle, Driving_licenses, Voivodeship


admin.site.register(Vehicle)
admin.site.register(Driving_licenses)
admin.site.register(Voivodeship)

urlpatterns = [
  path('admin/', admin.site.urls),
]
