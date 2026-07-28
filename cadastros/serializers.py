from rest_framework import serializers
from .models import Company, Branch, Sector, TicketType, TicketSubtype


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Company
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model  = Branch
        fields = '__all__'


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Sector
        fields = '__all__'


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TicketType
        fields = '__all__'


class TicketSubtypeSerializer(serializers.ModelSerializer):
    ticket_type_name = serializers.CharField(source='ticket_type.name', read_only=True)

    class Meta:
        model  = TicketSubtype
        fields = '__all__'