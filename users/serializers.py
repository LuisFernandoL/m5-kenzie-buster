from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(default=False)
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ],
    )
    username = serializers.CharField(
        max_length=150,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ],
    )
    is_superuser = serializers.BooleanField(default=False, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data: dict):
        if validated_data.get("is_employee", False):
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)

        return user

    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == "password":
                instance.set_password(value)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)
    username = serializers.CharField(max_length=150)
