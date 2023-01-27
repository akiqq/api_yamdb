from rest_framework import serializers

from .models import User
from .validators import validate_username


class UserSerializer(serializers.ModelSerializer):

    role = serializers.CharField(max_length=50, read_only=True)

    class Meta:
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        model = User
        lookup_field = 'username'


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        model = User


class SignUpSerializer(serializers.Serializer):

    username = serializers.CharField(
        max_length=150,
        validators=[validate_username]
    )
    email = serializers.EmailField(max_length=254)


class TokenSerializer(serializers.Serializer):

    username = serializers.CharField(
        max_length=150,
        validators=[validate_username]
    )
    confirmation_code = serializers.CharField()
