from rest_framework.serializers import ModelSerializer

from .models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'mobile',
            'company_name',
            'sales_contact_id',
            'customer_type',
        )
        read_only_fields = ['sales_contact_id']
    
    def create(self, validated_data) -> Customer:
        """assign the user request in the field sales_contact_id"""

        user = self.context["request"].user
        customer = Customer.objects.create(sales_contact_id=user, **validated_data)
        customer.save()

        return customer

