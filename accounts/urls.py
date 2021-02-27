from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("userRequests/", views.requests, name="requests"),
    path("accept/<user>", views.accept, name="accept")
]
