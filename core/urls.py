from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render


def home(request):
    return HttpResponse("Projeto Integrador Django - Sistema Online")


# 🔹 HTML de teste – PDF
def upload_pdf(request):
    return render(request, "upload_pdf.html")


# 🔹 HTML de teste – JSON
def upload_json(request):
    return render(request, "upload_json.html")


urlpatterns = [
    path("", home),

    # Admin
    path("admin/", admin.site.urls),

    # 🔥 PÁGINAS HTML DE TESTE
    path("test/pdf/", upload_pdf),
    path("test/json/", upload_json),

    # Grupo 2 - Auth
    path("auth/", include("apps.grupo2_auth.urls")),

    # Grupo 3 - Imagens
    path("images/", include("apps.grupo3_images.urls")),

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
