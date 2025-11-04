from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models import BaseModel


class Usuario(AbstractUser, BaseModel):

    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    meta_financeira = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )

    def __str__(self):
        return self.username
