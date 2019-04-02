from django.urls import path
from my_app import views

app_name = 'my_app'
urlpatterns = [
    path('login/', views.LoginView.as_view(tipo='Externo'), name='login'),
    # path('login/', views.login),
    path('home/', views.HomeView.as_view()),
    # path('home/', views.home),
    path('logout/', views.LogoutRedirectView.as_view()),
    # path('logout/', views.logout),
    path('teste/', views.TesteView.as_view()),
    path('addresses/', views.AdressListView.as_view(), name='address_list'),
    # path('addresses/', views.address_list, name='address_list'),
    path('addresses/<int:pk>/detail/', views.AddressDetail.as_view(), name='address-detail'),
    path('addresses/create/', views.address_create, name='address_create'),
    path('addresses/<int:id>/update/', views.address_update, name='address_update'),
    path('addresses/<int:id>/destroy/', views.address_destroy, name='address_destroy'),
]