from django.shortcuts import render
from django.http import HttpResponse
# from django.templateresponse import TemplateResponse

def movie(request):
    return render(request, 'first/index.html', {})

def room(request):
    return HttpResponse("Example room")

def index(request):
    return HttpResponse("Example message.")