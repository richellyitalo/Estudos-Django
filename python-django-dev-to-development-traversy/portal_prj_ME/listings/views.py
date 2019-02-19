from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import Listing

def index(request):
    listings_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings_list, 3)

    page = request.GET.get('page')
    listings = paginator.get_page(page)
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')