from django.urls import path

from backend import views

urlpatterns = [
    path("api/game/", views.GameListCreate.as_view()),
    path("api/game/<int:pk>", views.GameDetail.as_view()),
    path("api/image/<int:fk>", views.ImageViewSet.as_view({"get": "retrieve"})),
    path("api/review/<int:fk>", views.ReviewViewSet.as_view({"get": "retrieve"})),
]
