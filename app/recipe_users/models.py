"""
app.recipe_users.model
----------------------
Models file for handle recipe users
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .utils import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model User class
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
