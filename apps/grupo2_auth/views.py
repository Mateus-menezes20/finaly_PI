from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# =========================
# TELA HTML (GET)
# =========================
def login_page(request):
    """
    Renderiza a página de login (HTML)
    """
    return render(request, "grupo2_auth/login.html")


# =========================
# API DE LOGIN (POST)
# =========================
@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return JsonResponse(
                {"error": "Usuário e senha são obrigatórios"},
                status=400
            )

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return JsonResponse({"message": "Login realizado com sucesso"})

        return JsonResponse({"error": "Credenciais inválidas"}, status=401)

    # 👇 mantém comportamento correto para API
    return JsonResponse(
        {"error": "Método não permitido. Use POST."},
        status=405
    )


# =========================
# LOGOUT
# =========================
def logout_view(request):
    logout(request)
    return JsonResponse({"message": "Logout realizado"})
