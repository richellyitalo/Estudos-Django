from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/home.html')

def sobre(request):
    return render(request, 'pages/sobre.html')