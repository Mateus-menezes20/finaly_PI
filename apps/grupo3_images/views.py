from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import UploadedImage

@csrf_exempt
def upload_image(request):

    if request.method == "GET":
        return render(request, "grupo3_images/upload.html")

    if request.method == "POST":
        file = request.FILES.get("image")

        if not file:
            return JsonResponse({"error": "Nenhuma imagem enviada"}, status=400)

        img = UploadedImage.objects.create(image=file)

        return JsonResponse({
            "uuid": str(img.uuid),
            "url": img.image.url
        })

    return JsonResponse({"error": "Método não permitido"}, status=405)


def serve_image(request, uuid):
    try:
        img = UploadedImage.objects.get(uuid=uuid)
    except UploadedImage.DoesNotExist:
        raise Http404("Imagem não encontrada")

    return JsonResponse({
        "uuid": str(img.uuid),
        "image_url": img.image.url
    })
