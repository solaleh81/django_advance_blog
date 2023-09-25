from logging import exception
from rest_framework import serializers
from ...models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "password1"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError({"detail": "password doesnt match!"})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password1", None)
        return super().create(validated_data)
