from django.db import models
from django.conf import settings
from apps.core.models import BaseModel


class Carteira(BaseModel):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="Carteira"
    )
    nome = models.CharField(max_length=100, default="Carteira")
    saldo = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )

    def __str__(self):
        return f"{self.usuario.username} - {self.nome}"
