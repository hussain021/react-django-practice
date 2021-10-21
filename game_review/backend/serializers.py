from rest_framework import serializers

from backend.models import Game, Image, Review


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = serializers.ALL_FIELDS


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = serializers.ALL_FIELDS


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = serializers.ALL_FIELDS
