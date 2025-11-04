from django.db import models
from apps.carteira.models import BaseModel
from apps.carteira.models import Carteira


class Transacao(BaseModel):
    TIPO_CHOICES = [
        ('R', 'Receita'),
        ('D', 'Despesa'),
    ]

    carteira = models.ForeignKey(
        Carteira, on_delete=models.CASCADE, related_name="Transações"
    )
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.valor} ({self.descricao})"

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.tipo == 'R':
                self.carteira.saldo_inicial += self.valor
            elif self.tipo == 'D':
                self.carteira.saldo_inicial -= self.valor
            self.carteira.save()

        super().save(*args, **kwargs)
