from django import forms
from .models import StockEntry, Product


class StockEntryForm(forms.Form):
    amount = forms.IntegerField(label='Quantidade', required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=True,
                                     widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = StockEntry
