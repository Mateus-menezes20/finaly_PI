from django.http import JsonResponse
from django.shortcuts import redirect

PUBLIC_URLS = [
    "/admin/",
    "/auth/login/",
    "/auth/register/",
    "/accounts/login/",
]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        # 🔓 Libera URLs públicas
        for url in PUBLIC_URLS:
            if path.startswith(url):
                return self.get_response(request)

        # 🔓 Libera arquivos estáticos e media
        if path.startswith("/static/") or path.startswith("/media/"):
            return self.get_response(request)

        # 🔒 Bloqueia se não autenticado
        if not request.user.is_authenticated:
            return JsonResponse(
                {"error": "Usuário não autenticado"},
                status=401
            )

        return self.get_response(request)
