"""
app.recipe_users.tests.test_recipe_users_api
--------------------------------------------
Tests cases for recipe_users API functionality
"""
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from .tests_utils.constants import RecipeUserTestConstants
from .tests_utils.utils import get_user, create_user, filter_user


class TestRecipeUserPublicAPI(TestCase):
    """
    Test the public calls to the recipe_users API
    """

    def setUp(self) -> None:
        self.test_client = APIClient()

    def test_create_valid_user(self):
        """
        Test the successful creation of a user when the API is call with the
        correct  payload
        :return: None
        """
        test_payload = {
            'email': 'foo.pass1@bar.test',
            'password': 'MyPassword123',
            'name': 'Foo Bar',
        }

        test_response = self.test_client.post(
            RecipeUserTestConstants.CREATE_USER_URL.value,
            test_payload
        )
        self.assertEqual(test_response.status_code, status.HTTP_201_CREATED)
        test_created_user = get_user(**test_response.data)
        self.assertTrue(
            test_created_user.check_password(test_payload['password'])
        )
        self.assertNotIn('password', test_response.data)

    def test_create_duplicate_user(self):
        """
        Test creating a user when its already exists
        :return: None
        """
        test_payload = {
            'email': 'foo.test@bar.test',
            'password': 'MyTestPassword',
            'name': 'Foo Bar',
        }
        create_user(**test_payload)

        test_response = self.test_client.post(
            RecipeUserTestConstants.CREATE_USER_URL.value,
            test_payload
        )
        self.assertEqual(
            test_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_create_user_password_to_short(self):
        """
        Test creating a user when the password is to short. The password
        should be more than 8 characters
        :return: None
        """
        test_payload = {
            'email': 'foo.psswd@bar.test',
            'password': 'pwsdfds',
            'name': 'Foo Bar',
        }
        test_response = self.test_client.post(
            RecipeUserTestConstants.CREATE_USER_URL.value,
            test_payload
        )
        self.assertEqual(
            test_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        test_user_exists = filter_user(
            **{'email': test_payload['email']}
        ).exists()
        self.assertFalse(test_user_exists)

    def test_create_user_token(self):
        """
        Test the Creation of a user token
        :return: None
        """
        test_payload = {
            'email': 'foo.test@bar.test',
            'password': 'MyTestPassword',
            'name': 'Foo Bar',
        }
        create_user(**test_payload)
        test_response = self.test_client.post(
            RecipeUserTestConstants.TOKEN_URL.value,
            test_payload
        )
        self.assertEqual(test_response.status_code, status.HTTP_200_OK)
        self.assertIn('token', test_response.data)

    def test_create_user_token_invalid_credentials(self):
        """
        Test when a we give invalid creation to a retrieve token
        :return: None
        """
        create_user(
            **{
                'email': 'foo.test@bar.test',
                'password': 'MyTestPassword',
                'name': 'Foo Bar',
            }
        )
        test_payload = {
            'email': 'foo.test@bar.test',
            'password': 'WrongPassword',
            'name': 'Foo Bar',
        }
        test_response = self.test_client.post(
            RecipeUserTestConstants.TOKEN_URL.value,
            test_payload
        )
        self.assertEqual(
            test_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertNotIn('token', test_response.data)

    def test_create_token_no_user(self):
        """
        Test for the creation of token when the user doesn't exist
        :return: None
        """
        test_payload = {
            'email': 'foo.test@bar.test',
            'password': 'WrongPassword',
            'name': 'Foo Bar',
        }
        test_response = self.test_client.post(
            RecipeUserTestConstants.TOKEN_URL.value,
            test_payload
        )
        self.assertEqual(
            test_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertNotIn('token', test_response.data)

    def test_create_token_missing_field(self):
        """
        Test for the creation of token when the payload doesn't contains
        email nor password
        :return: None
        """
        test_response = self.test_client.post(
            RecipeUserTestConstants.TOKEN_URL.value,
            {}
        )
        self.assertEqual(
            test_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertNotIn('token', test_response.data)
