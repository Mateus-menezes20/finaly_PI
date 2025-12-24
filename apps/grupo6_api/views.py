from django.http import FileResponse, JsonResponse
from django.views.decorators.http import require_POST
from apps.grupo6_api.services.orchestrator import AnalysisOrchestrator
from apps.grupo5_reports.services.pdf_service import generate_pdf_report


@require_POST
def test_analyze(request):
    image_file = request.FILES.get("image")
    output_format = request.POST.get("format", "pdf")  # pdf | json

    if not image_file:
        return JsonResponse({"erro": "Imagem não enviada"}, status=400)

    # paciente fake só para teste
    patient = request.user if request.user.is_authenticated else None

    # 🔥 pipeline completo
    history = AnalysisOrchestrator.process(patient, image_file)

    # =========================
    # 🔁 RETORNO EM JSON
    # =========================
    if output_format == "json":
        return JsonResponse({
            "patient": str(patient) if patient else None,
            "image_id": history.image.id,
            "resultado": history.result,
            "criado_em": history.created_at
        }, safe=False)

    # =========================
    # 🔁 RETORNO EM PDF (default)
    # =========================
    pdf_path = generate_pdf_report(history)

    return FileResponse(
        open(pdf_path, "rb"),
        content_type="application/pdf",
        as_attachment=True,
        filename="relatorio_medico.pdf"
    )
