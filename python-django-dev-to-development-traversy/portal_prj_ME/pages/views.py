from django.shortcuts import render
from django.http import HttpResponse

from realtors.models import Realtor

def index(request):
    return render(request, 'pages/home.html')

def sobre(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/sobre.html', context)