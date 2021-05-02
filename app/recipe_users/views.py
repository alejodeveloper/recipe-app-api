"""
app.recipe_users.views
----------------------
Recipe User views
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """
    View for recipe users
    """
    serializer_class = UserSerializer


class TokenApiView(ObtainAuthToken):
    """
    Token API view class
    """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserApiView(generics.RetrieveUpdateAPIView):
    """
    Manage User API view
    """
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Retrieve user authenticated object
        :return: User instance model
        """
        return self.request.user
