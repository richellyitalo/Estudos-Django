from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Listing

# Create your views here.
def index(request):
    listings_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings_list, 2)

    page = request.GET.get('page')
    listings = paginator.get_page(page)
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
