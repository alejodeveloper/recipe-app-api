"""
app.recipe_users.test.tests_utils.constants
-------------------------------------------
Constants enums for test cases
"""
from enum import Enum
from django.urls import reverse


class RecipeUserTestConstants(Enum):
    CREATE_USER_URL = reverse('recipe_users:create')
    TOKEN_URL = reverse('recipe_users:token')
    ME_URL = reverse('recipe_users:me')
