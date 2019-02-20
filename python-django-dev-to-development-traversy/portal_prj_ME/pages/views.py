from django.shortcuts import render
from django.http import HttpResponse

from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices

def index(request):
    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
    }
    return render(request, 'pages/home.html', context)

def sobre(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/sobre.html', context)