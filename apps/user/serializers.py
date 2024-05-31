from .models import User
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.validators import ValidationError


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ImageField(source="profile.profile_photo")
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField(source="get_full_name")

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "gender",
            "password",
            "password2",
            "phone_number",
            "profile_photo",
            "is_active",
        ]

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self, obj):
        return obj.last_name.title()


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password", "password2"]

    def validate(self, attrs):
        """
        Check that the passwords are the same and should be at least 8 characters long
        """
        if attrs["password"] != attrs["password2"]:
            raise ValidationError("Passwords do not match")
        if len(attrs["password"]) < 8:
            raise ValidationError("Password should be at least 8 characters long")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"],
        )
        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    phone_number = PhoneNumberField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email is None:
            raise ValidationError("An email address is required to log in")

        if password is None:
            raise ValidationError("A password is required to log in")

        user = authenticate(request=self.context.get("request"), email=email, password=password)

        if user is None:
            raise ValidationError("A user with this email and password was not found")

        return {
            "email": user.email,
            "username": user.username,
            "phone_number": user.profile.phone_number,
            "id": user.pk,

        }
