from django.urls import path

from .views import (
    UserViewSet,
    RegistrationView,
    LoginView,
    MovieViewSet,
)

urlpatterns = [
    path("users/me", UserViewSet.as_view(), name="user"),
    path("signup", RegistrationView.as_view(), name="register"),
    path("signin", LoginView.as_view(), name="login"),
    path("movies", MovieViewSet.as_view(), name="movie"),
    # path("movies/<uuid:id>", MovieDeleteView.as_view(), name="delete"),
]
