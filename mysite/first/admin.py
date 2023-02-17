#Hello World!

from django.contrib import admin

# Register your models here.
from .models import Film, Screen, Screening, Booking

admin.site.register(Film)
admin.site.register(Screen)
admin.site.register(Screening)
admin.site.register(Booking)