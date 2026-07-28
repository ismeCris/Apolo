from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Company, Branch, Sector, TicketType, TicketSubtype
from .serializers import (
    CompanySerializer, BranchSerializer, SectorSerializer,
    TicketTypeSerializer, TicketSubtypeSerializer,
)


class IsAdminOrReadOnly(permissions.BasePermission):
    """Qualquer usuário autenticado pode ver (pra popular os selects do form de chamado).
    Só admin pode criar/editar/excluir."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_authenticated and getattr(request.user, 'role', None) == 'admin'


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminOrReadOnly]


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.select_related('company').all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminOrReadOnly]


class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    permission_classes = [IsAdminOrReadOnly]


class TicketTypeViewSet(viewsets.ModelViewSet):
    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer
    permission_classes = [IsAdminOrReadOnly]


class TicketSubtypeViewSet(viewsets.ModelViewSet):
    queryset = TicketSubtype.objects.select_related('ticket_type').all()
    serializer_class = TicketSubtypeSerializer
    permission_classes = [IsAdminOrReadOnly]