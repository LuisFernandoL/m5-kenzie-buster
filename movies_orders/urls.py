from django.urls import path
from . import views

urlpatterns = [
    path("movies/<int:movie_id>/orders/", views.MovieOrderView.as_view()),
]