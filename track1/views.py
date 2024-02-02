from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'track1/home.html')

def about(request):
    return HttpResponse('<h1>This tracks and does some interesting statistics</h1>')
# Create your views here.
