from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CategorySerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # user = serializers.StringRelatedField()
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='user')

    class Meta:
        model = Category
        # fields = '__all__'
        fields = ('id', 'name', 'description', 'user', 'user_id')
        # fields = ('id', 'name', 'description', 'created_at', 'updated_at')


# Serializer relacionados com categories apenas trazendo os IDS
# class ProductSerializer(serializers.ModelSerializer):
#     categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
#
#     class Meta:
#         model = Product
#         fields = ('name', 'price', 'categories')

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True,
                                                     many=True, source='categories')

    class Meta:
        model = Product
        fields = ('name', 'price', 'categories', 'category_id')
