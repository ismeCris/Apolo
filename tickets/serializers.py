from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    created_by_username  = serializers.CharField(source='created_by.username',  read_only=True)
    assigned_to_username = serializers.CharField(source='assigned_to.username', read_only=True)

    class Meta:
        model  = Ticket
        fields = '__all__'
        read_only_fields = (
            'id', 'created_by', 'created_at', 'updated_at',
            'created_by_username', 'assigned_to_username',
        )

    def validate(self, data):
        ticket_type = data.get('ticket_type', getattr(self.instance, 'ticket_type', None))
        due_date    = data.get('due_date', getattr(self.instance, 'due_date', None))

        # se for liberação de tela, o campo "tela" é obrigatório
        if ticket_type == Ticket.TicketType.LIBERAR_TELA:
            screen_name = data.get('screen_name', getattr(self.instance, 'screen_name', None))
            if not screen_name:
                raise serializers.ValidationError({
                    'screen_name': 'Informe o nome da tela quando o tipo for "Liberar Tela".'
                })

        # se preencher prazo, exige justificativa
        if due_date:
            justification = data.get(
                'deadline_justification',
                getattr(self.instance, 'deadline_justification', '')
            )
            if not justification:
                raise serializers.ValidationError({
                    'deadline_justification': 'Justifique o prazo solicitado.'
                })

        return data