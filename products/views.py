from rest_framework.generics import ListAPIView
from rest_framework import generics
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product


class CategoryListView(ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class ProductListView(ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class CategoryCreateView(generics.CreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class ProductCreateView(generics.CreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer