from rest_framework.views import APIView, status, Request, Response
from movies_orders.serializers import MovieOrderSerializer
from movies.models import Movie
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, req: Request, movie_id: int) -> Response:
        found_movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrderSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=req.user, movie=found_movie)
        return Response(serializer.data, status.HTTP_201_CREATED)
