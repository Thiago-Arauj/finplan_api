from rest_framework import viewsets
from apps.transacao.models import Transacao
from apps.transacao.api.v1.serializers import TransacaoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class TransacaoViewsets(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
