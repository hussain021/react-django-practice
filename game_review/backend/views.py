from rest_framework import generics, viewsets
from rest_framework.response import Response

from backend.models import Game, Image, Review
from backend.serializers import GameSerializer, ImageSerializer, ReviewSerializer


class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def retrieve(self, request, fk):
        queryset = Image.objects.filter(game_id=fk)
        serializer = ImageSerializer(queryset, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ImageSerializer

    def retrieve(self, request, fk):
        queryset = Review.objects.filter(game_id=fk)
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)
