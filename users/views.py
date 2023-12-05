from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status, Request, Response
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsUserAdmin
from rest_framework.permissions import IsAuthenticated


class LoginView(TokenObtainPairView):
    ...


class UserView(APIView):
    def get(self, req: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserAdmin]

    def get(self, req: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(req, found_user)
        serializer = UserSerializer(found_user)
        return Response(serializer.data)

    def patch(self, req: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(req, found_user)
        serializer = UserSerializer(found_user, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
