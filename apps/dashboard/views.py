from django.shortcuts import render
from .models import Funcionario

def dashboard(request):
    # Carrega todos funcionários ordenados por vendas
    funcionarios = Funcionario.objects.all().order_by('-vendas')
    return render(request, 'apps/dashboard/dashboard.html', {
        'funcionarios': funcionarios
    })