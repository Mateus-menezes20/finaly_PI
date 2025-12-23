from django.urls import path
from .views import login_view, logout_view, login_page

urlpatterns = [
    path("login/", login_view),        # API (POST)
    path("login/page/", login_page),   # HTML (GET)
    path("logout/", logout_view),
]
