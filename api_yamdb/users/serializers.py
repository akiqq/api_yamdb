from django.core.exceptions import ValidationError
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


class SignUpSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        max_length=150,
        validators=[validate_username]
    )
    email = serializers.EmailField(max_length=254)

    class Meta:
        fields = ('email', 'username')
        model = User

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError(
                "Me is not allowed"
            )
        user = User.objects.filter(username=data.get('username'))
        email = User.objects.filter(email=data.get('email'))
        if not user.exists() and email.exists():
            raise ValidationError("Недопустимый email")
        if user.exists() and user.get().email != data.get('email'):
            raise ValidationError("Недопустимый email")

        return data


class TokenSerializer(serializers.Serializer):

    username = serializers.CharField(
        max_length=150,
        validators=[validate_username]
    )
    confirmation_code = serializers.CharField()
