from django.contrib import admin
from .models import Film,Screen,Screening,Booking, Post

# Register your models here.


admin.site.register(Film)
admin.site.register(Screen)
admin.site.register(Screening)
admin.site.register(Booking)
admin.site.register(Post)
