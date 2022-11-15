from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Contract
from .serializers import ContractSerializer
from .permissions import ContractPermission
from .filters import ContractFilterSet


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [ContractPermission, IsAuthenticated]
    filterset_class = ContractFilterSet
