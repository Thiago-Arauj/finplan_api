from django.contrib import admin
from apps.usuario.models import Usuario
from apps.carteira.models import Carteira
from apps.transacao.models import Transacao

admin.site.register(Usuario)
admin.site.register(Carteira)
admin.site.register(Transacao)
