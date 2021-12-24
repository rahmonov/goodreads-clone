from django.urls import path

from users.views import RegisterView, LoginView


app_name = "users"
urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login")
]
