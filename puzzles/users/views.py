from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Puzzles va a ser la mejor aplicacion del mundo</h1>")
# Create your views here.
