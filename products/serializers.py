from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = [
      'id',
      'name',
      'description',
      'slug',
    ]


class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = [
      'name',
      'slug',
      'description',
      'price',
    ]
