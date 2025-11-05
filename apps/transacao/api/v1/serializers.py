from rest_framework import serializers
from rest_framework.exceptions import NotFound
from apps.transacao.models import Transacao


class TransacaoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # Get carteira from context (set in viewset)
        carteira = self.context.get('carteira')
        if carteira and not carteira.is_deleted:
            validated_data['carteira'] = carteira
        else:
            raise NotFound("Carteira inválida ou excluída.")

        return super().create(validated_data)

    class Meta:
        model = Transacao
        fields = '__all__'
        read_only_fields = ['carteira']
