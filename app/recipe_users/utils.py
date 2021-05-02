"""
app.recipe_users.utils
----------------------
Utils file to handle recipe users utilities functions
"""
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Manager class to perform users functions
    """

    def create_user(
            self,
            email: str,
            password: str = None,
            **more_args
    ):
        """
        Manager function to create a user
        :param email: Email of the user
        :param password: Password of the user can be none as well
        :param more_args: Another arguments in case we modify the user creation
        functionality
        :return: created user
        """
        if email is None:
            exception_message = "An email must be pass"
            raise ValueError(exception_message)

        new_user_creation_dict = {
            'email': self.normalize_email(email),
            **more_args
        }
        new_user = self.model(**new_user_creation_dict)
        new_user.set_password(password)
        new_user.save(using=self._db)

        return new_user

    def create_superuser(
            self,
            email: str,
            password: str = None,
            **more_args
    ):
        """
        Create a new super user for the app
        :param email: Email of the user
        :param password: Password of the user can be none as well
        :param more_args: Another arguments in case we modify the user creation
        functionality
        :return: New super user instance
        """
        new_superuser = self.create_user(email, password, **more_args)
        new_superuser.is_staff = True
        new_superuser.is_superuser = True
        new_superuser.save(using=self._db)

        return new_superuser
