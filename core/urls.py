from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("Projeto Integrador Django - Sistema Online")

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),

    # Grupo 2 - Autenticação
    path("auth/", include("apps.grupo2_auth.urls")),

    # Grupo 3 - Imagens
    path("images/", include("apps.grupo3_images.urls")),
    path("api/images/", include("apps.grupo3_images.urls")),

    # Grupo 4 - IA
    path("ai/", include("apps.grupo4_ai.urls")),

    # Grupo 5 - Relatórios
    path("reports/", include("apps.grupo5_reports.urls")),

    # Grupo 6 - API
    path("api/", include("apps.grupo6_api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
