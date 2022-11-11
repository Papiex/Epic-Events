from rest_framework.serializers import ModelSerializer
from rest_framework.generics import get_object_or_404


from .models import Event
from contracts.models import Contract
from customers.models import Customer


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = (
            "customer_id",
            "support_contact_id",
            "event_statut",
            "attendees",
            "event_date",
            "notes",
            "contract_id",
            "id",
        )
        read_only_fields = ["customer_id"]

    def create(self, validated_data) -> Event:
        """auto fill field customer_id with the customer in the contract"""
        contract = get_object_or_404(Contract, id=validated_data["contract_id"].id)
        customer = get_object_or_404(Customer, id=contract.customer_id.id)
        event = Event.objects.create(customer_id=customer, **validated_data)
        event.save()

        return event
