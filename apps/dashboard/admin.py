from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'vendas', 'data_cadastro')
    search_fields = ('nome', 'cpf')
    list_filter = ('data_cadastro',)
    ordering = ('-vendas',)
