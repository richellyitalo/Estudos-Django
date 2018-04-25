from django.urls import path

from . import views

app_name = 'enquete'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetalharView.as_view(), name='detalhar'),
    path('<int:pk>/resultados/', views.ResultadosView.as_view(), name='resultados'),
    path('<int:id_da_enquete>/view/', views.view, name='ver'),
    path('<int:id_pergunta>/votar', views.votar, name='votar')
]