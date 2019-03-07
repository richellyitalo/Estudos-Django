from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import Address
from .choices import STATE_CHOICES
from .forms import AddressForm


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


# Criação sem utilização do form orientado a objeto
# @login_required(login_url='/login/')
# def address_create(request):
#     if request.method == 'GET':
#         context = {
#             'states': STATE_CHOICES
#         }
#         return render(request, 'my_app/address/create.html', context)
#
#     # Post --> salvar
#     Address.objects.create(
#         address=request.POST.get('address'),
#         address_complement=request.POST.get('address_complement'),
#         city=request.POST.get('city'),
#         state=request.POST.get('state'),
#         country=request.POST.get('country'),
#         user=request.user
#     )
#
#     return redirect('/addresses/')

# Form orientado a objetos
# @login_required(login_url='/login/')
# def address_create(request):
#     form_submitted = False
#     if request.method == 'GET':
#         form = AddressForm()
#     else:
#         form_submitted = True
#         form = AddressForm(request.POST)
#         if form.is_valid():
#             Address.objects.create(
#                 address=form.cleaned_data['address'],
#                 address_complement=form.cleaned_data['address_complement'],
#                 city=form.cleaned_data['city'],
#                 state=form.cleaned_data['state'],
#                 country=form.cleaned_data['country'],
#                 user=request.user
#             )
#             return redirect('/addresses/')
#
#     return render(request, 'my_app/address/create.html', {'form': form, 'form_submitted': form_submitted})

# Form utilizando Model
@login_required(login_url='/login/')
def address_create(request):
    form_submitted = False
    if request.method == 'GET':
        form = AddressForm()
    else:
        form_submitted = True
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('my_app:address_list')

    return render(request, 'my_app/address/create.html', {'form': form, 'form_submitted': form_submitted})


# -------------------- update ---------------------
# Form não orientado a objeto
# @login_required(login_url='/login/')
# def address_update(request, id):
#     address = Address.objects.get(id=id)
#     if request.method == 'GET':
#         context = {
#             'states': STATE_CHOICES,
#             'address': address
#         }
#         return render(request, 'my_app/address/update.html', context)
#
#     # Post --> atualizar
#     address.address = request.POST.get('address')
#     address.address_complement = request.POST.get('address_complement')
#     address.city = request.POST.get('city')
#     address.state = request.POST.get('state')
#     address.country = request.POST.get('country')
#     address.save()
#
#     return redirect('/addresses/')

# Form orientado a objeto
# @login_required(login_url='/login/')
# def address_update(request, id):
#     form_submitted = False
#     address = Address.objects.get(id=id)
#     if request.method == 'GET':
#         form = AddressForm(address.__dict__)
#     else:
#         form_submitted = True
#         form = AddressForm(request.POST)
#         if form.is_valid():
#             address.address = form.cleaned_data['address']
#             address.address_complement = form.cleaned_data['address_complement']
#             address.city = form.cleaned_data['city']
#             address.state = form.cleaned_data['state']
#             address.country = form.cleaned_data['country']
#             address.save()
#
#             return redirect('/addresses/')
#     return render(request, 'my_app/address/update.html',
#                   {'address': address, 'form': form, 'form_submitted': form_submitted})

# Form utilizando Model
@login_required(login_url='/login/')
def address_update(request, id):
    form_submitted = False
    address = Address.objects.get(id=id)
    if request.method == 'GET':
        form = AddressForm(instance=address)
    else:
        form_submitted = True
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            address.save()
            return redirect('my_app:address_list')
    return render(request, 'my_app/address/update.html',
                  {'address': address, 'form': form, 'form_submitted': form_submitted})


@login_required(login_url='/login/')
def address_destroy(request, id):
    address = Address.objects.get(id=id)
    if request.method == 'GET':
        form = AddressForm(instance=address)
    else:
        address.delete()
        return redirect('my_app:address_list')

    context = {
        'address': address,
        'form': form
    }
    return render(request, 'my_app/address/destroy.html', context)
