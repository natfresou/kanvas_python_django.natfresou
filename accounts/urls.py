from django.urls import path
from . import views


urlpatterns = [
    path("accounts/", views.CreateAccountView.as_view()),
    path("login/", views.LoginView.as_view()),
]


