from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'city', 'state', 'realtor')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'city', 'state', 'description')
    list_filter = ('realtor',)

admin.site.register(Listing, ListingAdmin)