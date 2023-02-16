from django.contrib import admin

# Register your models here.
from .models import Movie, Screening

admin.site.register(Movie)
admin.site.register(Screening)

#admin.site.register(Screening)
