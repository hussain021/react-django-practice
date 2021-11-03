from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_jwt.settings import api_settings

from backend.models import Game, Image, Review, User


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = serializers.ALL_FIELDS


class DetailedGameSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Game
        fields = serializers.ALL_FIELDS


class SimpleGameSerializer(serializers.ModelSerializer):
    # This is a shorter serialzer for games, we call this on the home page.
    class Meta:
        model = Game
        fields = [
            "name",
            "id",
            "developer",
            "publisher",
            "poster_image",
            "description",
        ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = serializers.ALL_FIELDS


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class UserSerializerWithToken(serializers.ModelSerializer):
    """ 
        JWT referenced from here
        https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a
    """
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ("token", "username", "password")
