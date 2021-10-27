from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from backend.models import Game, Image, Review, User
from backend.serializers import (
    GameSerializer,
    ImageSerializer,
    ReviewSerializer,
    RegisterSerializer,
    GameTokenObtainPairSerializer,
)


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


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def retrieve(self, request, partial_name):
        queryset = Game.objects.filter(name__contains=partial_name).order_by("id")[:3]
        serializer = GameSerializer(queryset, many=True)
        return Response(serializer.data)


class PopularGamesViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def retrieve(self, request):
        queryset = Game.objects.all().order_by("all_reviews_count")[:20]
        serializer = GameSerializer(queryset, many=True)
        return Response(serializer.data)


class RecommendedGamesViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def retrieve(self, request):
        queryset = Game.objects.all().order_by("-all_reviews")[:10]
        serializer = GameSerializer(queryset, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ImageSerializer

    def retrieve(self, request, fk):
        queryset = Review.objects.filter(game_id=fk)
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = GameTokenObtainPairSerializer
