"""
app.recipe_users.tests.test_models
-------------------------------
Tests cases for recipe_users models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_username_successful(self):
        """
        Test a successfully user with email creation functionality
        :return: -> None
        """
        email = "foo@bar.test"
        password = "TestPass123"

        test_user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(test_user.email, email)
        self.assertTrue(test_user.check_password(password))

    def test_new_user_email_normalize(self):
        """
        Test the email for a new email user normalize
        :return: -> None
        """
        test_email = "foo@BAR.TEST"
        test_user = get_user_model().objects.create_user(email=test_email)
        self.assertEqual(test_user.email, test_email.lower())

    def test_new_user_invalid_email(self):
        """
        Test creating user with no email and raises an exception
        :return: -> None
        """
        with (self.assertRaises(ValueError)):
            get_user_model().objects.create_user(None, "123")

    def test_create_super_user(self):
        """
        Test whe we want to create a super user
        :return: -> None
        """

        test_user = get_user_model().objects.create_superuser(
            "foo@barr.test",
            'tesst123'
        )

        self.assertTrue(test_user.is_superuser)
        self.assertTrue(test_user.is_staff)
