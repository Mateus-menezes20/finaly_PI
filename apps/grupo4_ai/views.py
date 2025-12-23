from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services.ml_api import MLApiClient
from .models import AnalysisHistory

CLASS_MAPPING = {
    "malignant": "Maligno",
    "benign": "Benigno"
}

@csrf_exempt
def analyze_image(request):
    if request.method != "POST":
        return JsonResponse({"error": "Use POST"}, status=405)

    image_url = request.POST.get("image_url")

    if not image_url:
        return JsonResponse({"error": "image_url obrigatório"}, status=400)

    try:
        result = MLApiClient.predict(image_url)

        if "class" not in result or "confidence" not in result:
            return JsonResponse({"error": "Resposta inválida da IA"}, status=500)

        classification = CLASS_MAPPING.get(result["class"], "Desconhecido")
        confidence = float(result["confidence"])

        analysis = AnalysisHistory.objects.create(
            image_url=image_url,
            classification=classification,
            confidence=confidence,
            raw_response=result
        )

        return JsonResponse({
            "classification": classification,
            "confidence": confidence,
            "analysis_id": analysis.id
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
