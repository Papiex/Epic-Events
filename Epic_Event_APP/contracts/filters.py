from django_filters import rest_framework as filters

from contracts.models import Contract


class ContractFilterSet(filters.FilterSet):
    email = filters.CharFilter(field_name='customer_id__email')
    last_name = filters.CharFilter(field_name='customer_id__last_name')

    class Meta:
        model = Contract
        fields = [
            'amount',
            'payment_due',
            ]