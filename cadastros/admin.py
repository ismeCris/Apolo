from django.contrib import admin
from .models import Company, Branch, Sector, TicketType, TicketSubtype

admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Sector)
admin.site.register(TicketType)
admin.site.register(TicketSubtype)