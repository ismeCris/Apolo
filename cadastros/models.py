from django.db import models


class Company(models.Model):
    name    = models.CharField(max_length=150)
    cnpj    = models.CharField(max_length=20, blank=True)
    active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Branch(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='branches')
    name    = models.CharField(max_length=150)
    active  = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.company.name})'


class Sector(models.Model):
    name   = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class TicketType(models.Model):
    name   = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class TicketSubtype(models.Model):
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name='subtypes')
    name        = models.CharField(max_length=100)
    active      = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.ticket_type.name})'