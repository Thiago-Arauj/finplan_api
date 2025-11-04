from rest_framework import viewsets
from apps.carteira.models import Carteira
from .serializers import CarteiraSerializer
from rest_framework.permissions import IsAuthenticated


class CarteiraViewsets(viewsets.ModelViewSet):
    queryset = Carteira.objects.actives()
    serializer_class = CarteiraSerializer
    permission_classes = [IsAuthenticated]
