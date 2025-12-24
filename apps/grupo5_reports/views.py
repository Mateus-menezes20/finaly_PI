from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
from apps.grupo4_ai.models import AnalysisHistory
from .services.report_service import ReportService
import csv


@require_GET
def analysis_list(request):
    logs = AnalysisHistory.objects.all().values(
        "id",
        "created_at",
        "result"
    )
    return JsonResponse(list(logs), safe=False)


@require_GET
def analysis_stats(request):
    data = ReportService.analysis_stats()
    return JsonResponse(data)


@require_GET
def export_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="analises.csv"'

    writer = csv.writer(response)
    writer.writerow([
        "ID", "Data", "Resultado"
    ])

    for a in AnalysisHistory.objects.all():
        writer.writerow([
            a.id,
            a.created_at,
            a.result
        ])

    return response
