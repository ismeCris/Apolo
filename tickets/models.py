from django.db import models
from django.conf import settings


class Ticket(models.Model):
    class Status(models.TextChoices):
        OPEN        = 'open',        'Aberto'
        IN_PROGRESS = 'in_progress', 'Em andamento'
        WAITING     = 'waiting',     'Aguardando'
        RESOLVED    = 'resolved',    'Resolvido'
        CLOSED      = 'closed',      'Fechado'

    class Priority(models.TextChoices):
        LOW    = 'low',    'Baixa'
        MEDIUM = 'medium', 'Média'
        HIGH   = 'high',   'Alta'
        URGENT = 'urgent', 'Urgente'

    class TicketType(models.TextChoices):
        LIBERAR_TELA   = 'liberar_tela',   'Liberar Tela'
        RESET_SENHA    = 'reset_senha',    'Reset de Senha'
        ACESSO_SISTEMA = 'acesso_sistema', 'Acesso a Sistema'
        SUPORTE_GERAL  = 'suporte_geral',  'Suporte Geral'
        OUTRO          = 'outro',          'Outro'

    # --- campos existentes ---
    title       = models.CharField(max_length=200)
    description = models.TextField()
    status      = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    priority    = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets_created')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='tickets_assigned')
    created_at  = models.DateTimeField(auto_now_add=True)  # data/hora automática, não editável
    updated_at  = models.DateTimeField(auto_now=True)

    # --- novos campos ---
    ticket_type = models.CharField(
        max_length=20, choices=TicketType.choices, default=TicketType.SUPORTE_GERAL
    )  # tipo do chamado / assunto

    due_date = models.DateField(
        null=True, blank=True,
        help_text='Data prevista para conclusão do chamado'
    )  # data de previsão

    deadline_justification = models.TextField(
        blank=True,
        help_text='Justificativa do prazo solicitado'
    )  # justifique o prazo

    customer_sector = models.CharField(
        max_length=100, blank=True
    )  # setor do cliente

    company = models.CharField(max_length=150)   # empresa
    branch  = models.CharField(max_length=150)   # filial

    # campo condicional — só usado quando ticket_type == LIBERAR_TELA
    screen_name = models.CharField(
        max_length=150, blank=True, null=True,
        help_text='Nome da tela a ser liberada (obrigatório se tipo = Liberar Tela)'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'#{self.pk} — {self.title}'