from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Movie

from .serializer import UserSerializer, TokenSerializer, MovieSerializer
from .tokens.create_tokens import generate_access_token
from rest_framework import exceptions
from .tokens.auth import SafeJWTAuthentication

SALT = (
    "8b4f6b2cc1868d75ef79e5cfb8779c11b6a374bf0fce05b485581bf4e1e25b96c8c2855015de8449"
)


class RegistrationView(APIView):
    def post(self, request, format=None):
        request.data["password"] = make_password(
            password=request.data["password"], salt=SALT
        )

        exist_email = User.objects.filter(email=request.data["email"]).first()

        if exist_email:
            return Response(
                {
                    "success": False,
                    "message": "Пользователь с таким email уже существует",
                },
                status=status.HTTP_200_OK,
            )

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Теперь вы зарегистрированы на нашем сайте",
                },
                status=status.HTTP_200_OK,
            )

        else:
            error_msg = ""
            for key in serializer.errors:
                error_msg += serializer.errors[key][0]
            return Response(
                {
                    "success": False,
                    "message": error_msg,
                },
                status=status.HTTP_200_OK,
            )


class MovieViewSet(APIView):
    def get(self, request, format=None):
        cards = Movie.objects.all()
        serializer_movie = MovieSerializer(cards, many=True).data

        if cards is None:
            return Response(
                {
                    "success": False,
                    "message": "Фильм не найден",
                },
                status=status.HTTP_200_OK,
            )
            # print("serializer_movie : ", serializer_movie)

        else:
            return Response(serializer_movie, status=status.HTTP_200_OK)


class UserViewSet(APIView):
    def get(self, request, format=None):
        SafeJWTAuthentication.authenticate(self, request)
        user = request.user

        if user is None:
            return Response(
                {
                    "success": False,
                    "message": "Пользователь не найден",
                },
                status=status.HTTP_200_OK,
            )

        else:
            del user["password"]
            return Response(user, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request, format=None):
        email = request.data["email"]
        password = request.data["password"]
        hashed_password = make_password(password=password, salt=SALT)

        try:
            user = User.objects.get(email=email)
            print(user)
        except User.MultipleObjectsReturned:
            raise exceptions.AuthenticationFailed(
                "пользователь с таким email уже зарегистрирован"
            )

        if user is None or user.password != hashed_password:
            print("p")
            return Response(
                {
                    "success": False,
                    "message": "Нет такого пользователя",
                },
                status=status.HTTP_200_OK,
            )

        else:
            serializer_user = UserSerializer(user).data
            print("serializer_user: ", serializer_user)
            del serializer_user["password"]
            access_token = generate_access_token(serializer_user)
            token_obj = {
                "user_id": serializer_user["_id"],
            }
            serializer = TokenSerializer(data=token_obj)

            if serializer.is_valid():
                serializer.save()
            return Response(
                {
                    "user": serializer_user,
                    "token": access_token,
                },
                status=status.HTTP_200_OK,
            )
