from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import Address
from .choices import STATE_CHOICES


def login(request):
    context = {
        'app_path': request.get_full_path
    }
    if request.method == 'GET':
        return render(request, 'my_app/login.html', context)

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        # print(vars(user))
        django_login(request, user)

        # Redireciona caso haja next
        next_param = request.GET.get('next')
        if next_param:
            return redirect(next_param)
        return redirect('/home/')

    context['message'] = 'Dados inválidos'
    return render(request, 'my_app/login.html', context)


@login_required(login_url='/login/')
def logout(request):
    django_logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
def home(request):
    return render(request, 'my_app/home.html')


@login_required(login_url='/login/')
def address_list(request):
    addresses = Address.objects.all()
    context = {
        'addresses': addresses
    }
    return render(request, 'my_app/address/list.html', context)


@login_required(login_url='/login/')
def address_create(request):
    if request.method == 'GET':
        context = {
            'states': STATE_CHOICES
        }
        return render(request, 'my_app/address/create.html', context)

    # Post --> salvar
    Address.objects.create(
        address=request.POST.get('address'),
        address_complement=request.POST.get('address_complement'),
        city=request.POST.get('city'),
        state=request.POST.get('state'),
        country=request.POST.get('country'),
        user=request.user
    )

    return redirect('/addresses/')


@login_required(login_url='/login/')
def address_update(request, id):
    address = Address.objects.get(id=id)
    if request.method == 'GET':
        context = {
            'states': STATE_CHOICES,
            'address': address
        }
        return render(request, 'my_app/address/update.html', context)

    # Post --> atualizar
    address.address = request.POST.get('address')
    address.address_complement = request.POST.get('address_complement')
    address.city = request.POST.get('city')
    address.state = request.POST.get('state')
    address.country = request.POST.get('country')
    address.save()

    return redirect('/addresses/')
