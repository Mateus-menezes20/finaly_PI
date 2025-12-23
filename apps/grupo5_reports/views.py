from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
from .models import AuditLog
from .services.report_service import ReportService
from apps.grupo4_ai.models import AnalysisHistory
import csv

@require_GET
def analysis_list(request):
    logs = AnalysisHistory.objects.all().values(
        "id",
        "image_url",
        "classification",
        "confidence",
        "created_at"
    )

    AuditLog.objects.create(
        user=request.user if request.user.is_authenticated else None,
        action="Listou análises",
        endpoint="/reports/analyses/"
    )

    return JsonResponse(list(logs), safe=False)


@require_GET
def analysis_stats(request):
    data = ReportService.analysis_stats()

    AuditLog.objects.create(
        user=request.user if request.user.is_authenticated else None,
        action="Consultou estatísticas",
        endpoint="/reports/stats/"
    )

    return JsonResponse(data)


@require_GET
def export_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="analises.csv"'

    writer = csv.writer(response)
    writer.writerow([
        "ID", "Imagem", "Classificação",
        "Confiança", "Data"
    ])

    for a in AnalysisHistory.objects.all():
        writer.writerow([
            a.id,
            a.image_url,
            a.classification,
            a.confidence,
            a.created_at
        ])

    AuditLog.objects.create(
        user=request.user if request.user.is_authenticated else None,
        action="Exportou CSV",
        endpoint="/reports/export/csv/"
    )

    return response
