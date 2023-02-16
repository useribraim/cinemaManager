from django.contrib import admin
from django.urls import include, path
from first import views

urlpatterns = [
    path('movie/', views.movie, name='movie'),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]