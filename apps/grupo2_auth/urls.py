from django.urls import path
from .views import (
    login_page,
    register_page,
    login_view,
    register_view,
    logout_view
)

urlpatterns = [
    # HTML
    path("login/page/", login_page),
    path("register/page/", register_page),

    # API
    path("login/", login_view),
    path("register/", register_view),
    path("logout/", logout_view),
]
