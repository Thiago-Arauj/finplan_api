from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.transacao.models import Transacao
from apps.transacao.api.v1.serializers import TransacaoSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Q


class TransacaoViewsets(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='somar-transacoes')
    def somar_transacoes(self, request):
        """
        Retorna o total de receitas e despesas do usuário autenticado
        """
        user = request.user

        # Filtra as transações do usuário autenticado
        transacoes_usuario = Transacao.objects.filter(usuario=user)

        # Calcula o total de receitas (entradas)
        total_receitas = transacoes_usuario.filter(
            tipo='receita'
        ).aggregate(
            total=Sum('valor')
        )['total'] or 0

        # Calcula o total de despesas (saídas)
        total_despesas = transacoes_usuario.filter(
            tipo='despesa'
        ).aggregate(
            total=Sum('valor')
        )['total'] or 0

        # Calcula o saldo (receitas - despesas)
        saldo = total_receitas - total_despesas

        data = {
            'total_receitas': float(total_receitas),
            'total_despesas': float(total_despesas),
            'saldo': float(saldo),
            'usuario': user.username
        }

        return Response(data, status=status.HTTP_200_OK)
