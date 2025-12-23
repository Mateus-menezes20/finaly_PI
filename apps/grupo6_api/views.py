from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services.orchestrator import AnalysisOrchestrator


@csrf_exempt
def analyze(request):
    if request.method != "POST":
        return JsonResponse({"error": "Use POST"}, status=405)

    image_file = request.FILES.get("image")

    if not image_file:
        return JsonResponse({"error": "Imagem obrigatória"}, status=400)

    history = AnalysisOrchestrator.process(
        patient=None,
        image_file=image_file
    )

    return JsonResponse({
        "classification": history.classification,
        "confidence": history.confidence
    })
