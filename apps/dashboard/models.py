from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=False) # Ex: 123.456.789-00
    vendas = models.PositiveIntegerField(default=0)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['-vendas']
