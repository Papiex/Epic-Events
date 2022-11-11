import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from events.models import Event
from contracts.models import Contract


pytestmark = pytest.mark.django_db


class TestGetEndpoint:
    def test_should_get_list(
        self, api_client, create_contract, support_user, create_customer, saler_user
    ):
        """test get list with saler user"""
        unique_contract = Contract.objects.create(
            sales_contact_id=saler_user,
            customer_id=create_customer,
            status=False,
            amount=25.80,
            payment_due="2023-03-29T13:34:00.00Z",
        )
        payload = {
            "customer_id": create_customer,
            "support_contact_id": support_user,
            "event_statut": True,
            "attendees": 42,
            "event_date": "2023-03-29T13:34:00.00Z",
            "notes": "notes",
            "contract_id": create_contract,
        }
        Event.objects.create(**payload)
        payload["contract_id"] = unique_contract
        Event.objects.create(**payload)
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.get(f"/events/")

        assert response.status_code == 200
        assert len(Event.objects.all()) == 2

    def test_should_get_detail(self, api_client, create_event, saler_user):
        """test get detail with saler user"""
        event_object = create_event
        event_db = Event.objects.all().first()
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.get(f"/events/{event_object.id}/")
        data = response.data

        assert response.status_code == 200
        assert data["support_contact_id"] == event_db.support_contact_id.id
        assert data["event_statut"] == event_db.event_statut
        assert data["attendees"] == event_db.attendees
        assert data["notes"] == event_db.notes
        assert data["event_date"] == "2023-03-29T13:34:00Z"
        assert data["contract_id"] == event_db.contract_id.id
