from django.urls import path
from .views import analyze_image

urlpatterns = [
    path("analyze/", analyze_image),
]
