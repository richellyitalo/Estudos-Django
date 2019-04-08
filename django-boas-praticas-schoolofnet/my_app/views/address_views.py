from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from my_app.forms import AddressForm
from my_app.models.address import Address


@login_required(login_url='/login/')
def address_list(request):
    addresses = Address.objects.all()
    context = {
        'addresses': addresses
    }
    return render(request, 'my_app/address/list.html', context)


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