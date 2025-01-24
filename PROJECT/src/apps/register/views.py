from django.shortcuts import render, redirect
from django.contrib import messages
from apps.dashboard.models import UserTable

def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Verificação básica de campos obrigatórios
        if not name or not email or not password:
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, 'register/register.html')

        # Verificar se o email já está em uso
        if UserTable.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está registrado.")
            return render(request, 'register/register.html')

        # Criar o usuário
        try:
            UserTable.objects.create(name=name, email=email, password=password)
            messages.success(request, "Usuário registrado com sucesso!")
            return redirect('login')  # Substitua pelo nome da sua view de login
        except Exception as e:
            messages.error(request, f"Erro ao criar usuário: {str(e)}")
            return render(request, 'register/register.html')

    return render(request, 'register/register.html')
