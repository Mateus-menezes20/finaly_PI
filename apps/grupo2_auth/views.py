from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# =========================
# TELA HTML - LOGIN
# =========================
def login_page(request):
    return render(request, "grupo2_auth/login.html")


# =========================
# TELA HTML - REGISTER
# =========================
def register_page(request):
    return render(request, "grupo2_auth/register.html")


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

    return JsonResponse(
        {"error": "Método não permitido. Use POST."},
        status=405
    )


# =========================
# API DE REGISTRO (POST)
# =========================
@csrf_exempt
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return JsonResponse(
                {"error": "Usuário e senha são obrigatórios"},
                status=400
            )

        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {"error": "Usuário já existe"},
                status=400
            )

        user = User.objects.create_user(
            username=username,
            password=password
        )

        return JsonResponse(
            {
                "message": "Usuário criado com sucesso",
                "user_id": user.id
            },
            status=201
        )

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
