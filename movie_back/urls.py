from django.urls import path

from .views import RegistrationView, UserViewSet

urlpatterns = [
    path("users/me", UserViewSet.as_view(), name="user"),
    path("signup", RegistrationView.as_view(), name="register"),
    # path("signin", LoginView.as_view(), name="login"),
]
