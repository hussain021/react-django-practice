from django.urls import path

from backend import views

urlpatterns = [
    path("api/games/", views.GameListCreate.as_view(), name="all_games"),
    path(
        "api/games/popular-games",
        views.PopularGamesViewSet.as_view({"get": "retrieve"}),
        name="popular_games",
    ),
    path(
        "api/games/recommended-games",
        views.RecommendedGamesViewSet.as_view({"get": "retrieve"}),
        name="recommended_games",
    ),
    path("api/games/<int:pk>", views.GameDetail.as_view(), name="game_detail"),
    path(
        "api/image/<int:fk>",
        views.ImageViewSet.as_view({"get": "retrieve"}),
        name="game_images",
    ),
    path(
        "api/review/<int:fk>",
        views.ReviewViewSet.as_view({"get": "retrieve"}),
        name="game_reviews",
    ),
    path(
        "api/games-search/<str:partial_name>",
        views.GamesViewSet.as_view({"get": "retrieve"}),
        name="game_list",
    ),
]
