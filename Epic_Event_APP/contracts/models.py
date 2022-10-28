from django.db import models

from users.models import User
from customers.models import Customer


class Contract(models.Model):
    sales_contact_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField(blank=False)
    payment_due = models.DateTimeField(blank=False)
