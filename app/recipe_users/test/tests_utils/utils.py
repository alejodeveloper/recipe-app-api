"""
app.recipe_users.test.tests_utils.utils
---------------------------------------
Utils for recipe_users app test cases
"""
from django.contrib.auth import get_user_model


def create_user(**params):
    """
    Util function to create user and avoid all the objects sentence
    :param params: Dict parameters for recipe user creation
    :return: Recipe user instance
    """
    return get_user_model().objects.create_user(**params)


def get_user(**params):
    """
    Util function to get user and avoid all the objects sentence
    :param params: Dict parameters for recipe user creation
    :return: Recipe user instance
    """
    return get_user_model().objects.get(**params)


def filter_user(**params):
    """
    Util function to filter user and avoid all the objects sentence
    :param params: Dict parameters for recipe user creation
    :return: Recipe user queryset
    """
    return get_user_model().objects.filter(**params)
