from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from backend.models import Game
from backend.serializers import (
    GameSerializer,
    GameShorterSerializer,
    UserSerializerWithToken,
)

class GameViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        recommendedQueryset = Game.objects.all().order_by("-all_reviews_ratings")[:3]
        popularQueryset = Game.objects.all().order_by("all_reviews_count")[:20]
        serializer = GameShorterSerializer(recommendedQueryset.union(popularQueryset), many=True)
        return Response(serializer.data)
        
    def retrieve(self, request, pk):
        queryset = Game.objects.get(basemodel_ptr_id=pk)
        Serializer = GameSerializer(queryset)
        return Response(Serializer.data)


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def retrieve(self, request, partial_name):
        queryset = Game.objects.filter(name__contains=partial_name).order_by("id")[:3]
        serializer = GameSerializer(queryset, many=True)
        return Response(serializer.data)

class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
