from django.urls import path

from backend import views

urlpatterns = [
    path("api/games/", views.GameViewSet.as_view({"get": "list"}), name="all_games"),
    path(
        "api/games/<int:pk>",
        views.GameViewSet.as_view({"get": "retrieve"}),
        name="game_detail",
    ),
    path(
        "api/games-search/<str:partial_name>",
        views.SearchViewSet.as_view({"get": "retrieve"}),
        name="game_list",
    ),
]
