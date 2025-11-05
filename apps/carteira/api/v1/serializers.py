from rest_framework import serializers
from apps.carteira.models import Carteira


class CarteiraSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # Get user from context
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Carteira
        fields = [
            'id',
            'usuario',
            'nome',
            'saldo',
            'is_deleted',
        ]
        read_only_fields = [
            'usuario',
            'created_at',
            'updated_at',
            'deleted_at'
        ]
