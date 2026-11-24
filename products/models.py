from django.db import models


class Category(models.Model):
  name = models.CharField(
    max_length=100,
    unique=True
  )

  slug = models.SlugField(
    unique=True
  )
  
  description = models.TextField(
    blank=True
  )

  created_at = models.DateTimeField(
    auto_now_add=True
  )

  updated_at = models.DateTimeField(
    auto_now=True
  )
    
  def __str__(self):
    return self.name



class Product(models.Model):
  name = models.CharField(
    max_length=150
  )

  category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name='products'
  )

  slug = models.SlugField(
    unique=True
  )

  description = models.TextField(
    blank=True
  )

  price = models.DecimalField(
    decimal_places=2,
    max_digits=10
  )

  stock = models.PositiveIntegerField(
    default=0
  )

  image = models.ImageField()

  is_active = models.BooleanField(
    default=True
  )

  created_at = models.DateTimeField(
    auto_now_add=True
  )

  updated_at = models.DateTimeField(
    auto_now=True
  )

  def __str__(self):
    return self.name