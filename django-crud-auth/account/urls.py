from django.urls import path

# from . import views
from .views import (
    login_request,
    register_request,
    logout_request,
    change_password,
)

urlpatterns = [
    path("login", login_request, name="account_login"),  # account/login
    path("register", register_request, name="account_register"),  # account/register
    path("logout", logout_request, name="account_logout"),  # account/logout
    path(
        "change_password", change_password, name="account_change_password"
    ),  # account/change_password
]
