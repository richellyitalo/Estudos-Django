from rest_framework import viewsets, pagination
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product


class CustomPagination(pagination.PageNumberPagination):
    page_size = 1
    page_query_param = 'pagina'
    max_page_size = 5


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CustomPagination


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
