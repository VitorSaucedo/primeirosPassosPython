import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from apps.dashboard.models import Funcionario
from django.utils import timezone

dados_funcionarios = [
    {'nome': 'João Silva', 'cpf': '111.222.333-44', 'vendas': 150},
    {'nome': 'Maria Oliveira', 'cpf': '222.333.444-55', 'vendas': 200}, 
    {'nome': 'Pedro Souza', 'cpf': '333.444.555-66', 'vendas': 90},
    {'nome': 'Ana Costa', 'cpf': '444.555.666-77', 'vendas': 180},
    {'nome': 'Carlos Rocha', 'cpf': '555.666.777-88', 'vendas': 120}
]

for func in dados_funcionarios:
    Funcionario.objects.create(**func)

print("Dados de teste criados com sucesso!")