from django.db import models

from users.models import User
from customers.models import Customer
from contracts.models import Contract

class Event(models.Model):
    """"""
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    event_statut_id = models.BooleanField(default=False, blank=False)
    attendees = models.IntegerField(blank=False)
    event_date = models.DateTimeField(blank=False)
    notes = models.TextField(max_length=250)
    contract_id = models.OneToOneField(Contract, on_delete=models.CASCADE, blank=False)