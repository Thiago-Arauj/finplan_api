from django.db import models
from django.utils import timezone

# Create your models here.

class BaseQuerySet(models.QuerySet):
    # Função que retorna só os ativos
    def actives(self):
        return self.filter(is_deleted=False)

    # Função para retornar ativos e deletados
    def with_deleted(self):
        return self.all()


# Manager para associar aos modelos
class BaseManager(models.Manager):
    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()

    def with_deleted(self):
        return self.get_queryset().all()


class BaseModel(models.Model):
    # Atributos para Auditoria
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # soft delete
    is_deleted = models.BooleanField(default=False)
    # registro do soft delete para auditoria
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Novo gerenciador do soft delete
    objects = BaseManager()

    class Meta:
        abstract = True

    # Realiza soft delete sem remover do banco
    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    # Restaura o registro deletado
    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()