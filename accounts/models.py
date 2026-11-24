from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(
    unique=True,
    db_index=True
  )

  first_name = models.CharField(
    max_length=100
  )

  last_name = models.CharField(
    max_length=100
  )

  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=True)

  objects = CustomUserManager()

  USERNAME_FIELD = "email"

  REQUIRED_FIELDS = ["first_name", "last_name"]

  def __str__(self):
      return self.email