from django.urls import path
from .views import upload_image, serve_image

urlpatterns = [
    path("upload/", upload_image),
    path("<uuid:uuid>/", serve_image),
]
