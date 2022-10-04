from django.db import models

from users.models import User


class Customer(models.Model):
    """Define client model"""
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    email = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    mobile = models.CharField(max_length=20, blank=False)
    company_name = models.CharField(max_length=250, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
