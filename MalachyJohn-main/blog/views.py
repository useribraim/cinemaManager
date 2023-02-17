from django.shortcuts import render
from django.views.generic import ListView
from .models import Screening,Film,Post

# Create your views here.

class BlogListView(ListView):
    model=Screening  
    template_name="home.html"