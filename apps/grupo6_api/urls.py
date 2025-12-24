from django.urls import path
from .views import test_analyze

urlpatterns = [
    path("test-analyze/", test_analyze),
]
