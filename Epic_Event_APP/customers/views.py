from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets

from .models import Customer
from .serializers import CustomerSerializer
from .permissions import IsSalerCustomerOrReadOnly


class CustomerViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsSalerCustomerOrReadOnly]

