from django.urls import path

from my_app.views import auth_views, address_views, default_views

app_name = 'my_app'
urlpatterns = [
    path('login/', auth_views.login),
    path('home/', default_views.home),
    path('logout/', auth_views.logout),
    path('addresses/', address_views.address_list, name='address_list'),
    path('addresses/create/', address_views.address_create, name='address_create'),
    path('addresses/<int:id>/update/', address_views.address_update, name='address_update'),
    path('addresses/<int:id>/destroy/', address_views.address_destroy, name='address_destroy'),
]
