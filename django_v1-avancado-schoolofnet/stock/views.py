from django.shortcuts import render, redirect
from .models import StockEntry
from .forms import StockEntryForm


def entries_list(request):
    results = StockEntry.objects.all()

    return render(request, 'stock/entries/list.html', {
        'entries': results
    })


def entries_new(request):
    return render(request, 'stock/entries/new.html', {
        'form': StockEntryForm()
    })


def entries_create(request):
    form = StockEntryForm(request.POST)
    if form.is_valid():
        StockEntry.objects.create(
            amount=form.cleaned_data['amount'],
            product=form.cleaned_data['product']
        )
    return redirect('stock-entries')
