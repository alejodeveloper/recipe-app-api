"""
app.recipe_users.tests.test_recipe_users_admin
----------------------------------------------
Tests cases for recipe_users admin functionality
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class TestRecipeUsersAdmin(TestCase):
    """
    Test cases for recipe_users admin
    """

    def setUp(self) -> None:
        self.test_client = Client()
        self.test_admin_user = get_user_model().objects.create_superuser(
            email='test_admin.foo@bar.test',
            password='Passwd123'
        )
        self.test_client.force_login(self.test_admin_user)
        self.test_user = get_user_model().objects.create_user(
            email='foo@bar.test',
            password='Passwd123',
            name='Foo Bar Test'
        )

    def test_users_admin_listed(self):
        """
        Test that the users are listed on the users admin page
        :return: None
        """
        test_url = reverse('admin:recipe_users_user_changelist')
        test_response = self.test_client.get(test_url)

        self.assertContains(test_response, self.test_user.name)
        self.assertContains(test_response, self.test_user.email)

    def test_admin_users_page_change(self):
        """
        Test the admin user page works
        :return: None
        """

        test_url = reverse(
            'admin:recipe_users_user_change',
            args=[self.test_user.id]
        )
        test_response = self.test_client.get(test_url)

        self.assertEqual(test_response.status_code, 200)

    def test_admin_create_user(self):
        """
        Test that the admin create user page works
        :return: None
        """

        test_url = reverse('admin:recipe_users_user_add')
        test_response = self.test_client.get(test_url)
        self.assertEqual(test_response.status_code, 200)
