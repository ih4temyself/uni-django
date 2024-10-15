# loginregister/serializers.py
import re

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    password_check = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password_check",
        ]

    def validate(self, data):
        if data["password"] != data["password_check"]:
            raise serializers.ValidationError("Passwords do not match")
        if len(data["password"]) < 8 or not re.search(r"\d", data["password"]):
            raise serializers.ValidationError(
                "Password must be at least 8 characters long and contain a number."
            )

        if not re.match(r"[^@]+@[^@]+\.[^@]+", data["email"]):
            raise serializers.ValidationError("Invalid email address")

        return data

    def create(self, validated_data):
        validated_data.pop("password_check")
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )
        return user
