from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# from django.contrib.auth import get_user_model
# User = get_user_model()
from .models import CustomUser, StudentUser


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('phone', 'password')
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user



class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'isAdmin', 'user_type']

    def get_isAdmin(self, obj):
        return obj.is_staff



class UserSerialiserWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'isAdmin', 'user_type', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class StudentRegisterSerial(serializers.ModelSerializer):
    # roll_number = serializers.

    class Meta:
        model = CustomUser