from rest_framework.serializers import ModelSerializer

from .models import Contract


class ContractSerializer(ModelSerializer):
    """"""
    class Meta:
        model = Contract
        fields = (
            'sales_contact_id',
            'customer_id',
            'status',
            'amount',
            'payment_due'
        )
        read_only_fields = ['sales_contact_id']

    def create(self, validated_data) -> Contract:
        """assign the user request in the field sales_contact_id"""

        user = self.context["request"].user
        contract = Contract.objects.create(sales_contact_id=user, **validated_data)
        contract.save()
        
        return contract