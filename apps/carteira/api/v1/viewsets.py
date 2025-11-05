from rest_framework import viewsets
from apps.carteira.models import Carteira
from .serializers import CarteiraSerializer
from rest_framework.permissions import IsAuthenticated


class CarteiraViewsets(viewsets.ModelViewSet):
    queryset = Carteira.objects.actives()  # Default queryset
    serializer_class = CarteiraSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def get_queryset(self):
        if self.action in ['update', 'partial_update']:
            # Custom queryset for update operations
            return Carteira.objects.with_deleted()
        else:
            # Default queryset for other actions
            return Carteira.objects.actives()
