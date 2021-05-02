"""
app.recipe_app.management.commands.wait_for_db
----------------------------------------------
Wait for DB connection command
"""
import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Django command to pause execution until db is available
    """

    def handle(self, *args, **options):
        """
        Run the management command
        :return: None
        """
        self.stdout.write('Waiting For Database connection...')
        db_conn = None
        while db_conn is None:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable... waiting...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!!!'))
