from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework import exceptions

from .serializer import UserSerializer, TokenSerializer, MovieSerializer
from .models import User, Movie
from .tokens.auth import SafeJWTAuthentication
from .tokens.create_tokens import generate_access_token, generate_refresh_token

SALT = (
    "8b4f6b2cc1868d75ef79e5cfb8779c11b6a374bf0fce05b485581bf4e1e25b96c8c2855015de8449"
)


class RegistrationView(APIView):
    def post(self, request, format=None):
        password = request.data["password"]
        request.data["password"] = make_password(password=password, salt=SALT)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Теперь вы зарегистрированы на нашем сайте!",
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
        if cards is None:
            return Response(
                [],
                status=status.HTTP_200_OK,
            )

        else:
            serializer_card = MovieSerializer(cards, many=True).data
            return Response(serializer_card, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        if request.method == "POST":
            user = SafeJWTAuthentication.authenticate(self, request)[0]

            request.data["owner"] = user["_id"]

            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                card = Movie.objects.get(nameEN=request.data["nameEN"])
                serializer_card = MovieSerializer(card).data
                return Response(serializer_card, status=status.HTTP_200_OK)

            else:
                return Response(
                    {
                        "success": False,
                        "message": "Данные карты невалидны",
                    },
                    status=status.HTTP_200_OK,
                )


class MovieDeleteView(APIView):
    def delete(self, request, id, format=None):
        cards = Movie.objects.all()
        if request.method == "DELETE":
            SafeJWTAuthentication.authenticate(self, request)
            if cards:
                Movie.objects.filter(_id=id).delete()
                serializer = MovieSerializer(cards, many=True).data
                return Response(serializer, status=status.HTTP_200_OK)


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

    def patch(self, request, format=None):
        if request.method == "PATCH":
            serializer, user = SafeJWTAuthentication.authenticate(self, request)
            print(serializer)

            name = request.data["name"]
            email = request.data["email"]
            print(email)

            serializer["name"] = name
            serializer["email"] = email

            serializer_user = UserSerializer(user, data=serializer, partial=True)

            if serializer_user.is_valid():
                serializer_user.save()
                return Response(serializer, status=status.HTTP_200_OK)

            else:
                return Response(
                    {
                        "success": False,
                        "message": "Данные пользователя не валидны",
                    },
                    status=status.HTTP_200_OK,
                )


class LoginView(APIView):
    def post(self, request, format=None):
        email = request.data["email"]
        password = request.data["password"]
        hashed_password = make_password(password=password, salt=SALT)

        try:
            user = User.objects.get(email=email)
        except User.MultipleObjectsReturned:
            raise exceptions.AuthenticationFailed(
                "пользователь с таким email уже зарегистрирован"
            )

        if user is None or user.password != hashed_password:
            return Response(
                {
                    "success": False,
                    "message": "Пользователь не найден",
                },
                status=status.HTTP_200_OK,
            )

        else:
            serializer_user = UserSerializer(user, many=False).data
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
                    "token": access_token,
                    "user": serializer_user,
                },
                status=status.HTTP_200_OK,
            )
