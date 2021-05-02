"""
app.recipe_users.serializers
----------------------------
Serializers for recipe_users app
"""
from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Model user serializer for recipe_users User model
    """

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name',)
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        """
        Create a new user
        :param validated_data:
        :return: User model instance
        """
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """
        Serializer method for update recipe user
        :param instance:
        :param validated_data:
        :return: User model instance
        """
        password = validated_data.pop('password', None)
        updated_user = super().update(instance, validated_data)
        if password:
            updated_user.set_password(password)
            updated_user.save()

        return updated_user


class AuthTokenSerializer(serializers.Serializer):
    """
    Token serializer for recipe users
    """
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_style': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """
        Validate and authenticate the user
        :param attrs: different attributes for the user that came in the
        serializer
        :return: User validated and authenticated
        """
        email = attrs.get('email')
        password = attrs.get('password')

        authenticated_user = authenticate(
            request=self.context.get('context'),
            username=email,
            password=password
        )
        if not authenticated_user:
            error_message = 'Unable to authenticate with provide credentials'
            raise serializers.ValidationError(
                error_message, code='authentication'
            )
        attrs['user'] = authenticated_user
        return attrs
