"""
app.recipe_app.tests.test_commands
-----------------------------------
Tests cases for django commands
"""
from unittest.mock import patch
from django.test import TestCase
from django.core.management import call_command
from django.db.utils import OperationalError


class TestCommands(TestCase):

    def test_wait_for_db_ready(self):
        """
        Test for waiting until the db is available
        :return: None
        """

        with patch(
                'django.db.utils.ConnectionHandler.__getitem__',
                return_value=True
        ) as gi:
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db_command_(self, mock_time_sleep):
        """
        Test waiting for the db connection
        :return: None
        """
        with patch(
                'django.db.utils.ConnectionHandler.__getitem__',
                side_effect=[OperationalError]*5 + [True]
        ) as gi:
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
