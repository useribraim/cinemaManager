from django.contrib import admin
from django.urls import include, path
from first import views

urlpatterns = [
    path('movie/', views.movie, name='movie'),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),

    #may not work as expected without this.
    #path("",FirstListView.as_view(),name="home")
]