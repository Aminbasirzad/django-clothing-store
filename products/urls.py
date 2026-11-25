from django.urls import path
from .views import CategoryListView, ProductListView, ProductCreateView, CategoryCreateView

urlpatterns = [
  path('categories/', CategoryListView.as_view(), name='categories'),
  path('products/', ProductListView.as_view(), name='products'),
  path('categories/create/', CategoryCreateView.as_view(), name='categories_create'),
  path('products/create/', ProductCreateView.as_view(), name='products_create'),
]