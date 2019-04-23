from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog.index'),
    path('show/<int:id>/', views.show, name='blog.show'),
]