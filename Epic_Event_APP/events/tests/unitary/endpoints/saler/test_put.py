import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from contracts.models import Contract
from events.models import Event


pytestmark = pytest.mark.django_db


class TestPutEndpoint:
    def test_should_update(
        self, create_contract, create_event, saler_user, api_client, support_user
    ):
        """test update with gestion_user"""
        event_object = create_event
        payload = {
            "support_contact_id": support_user.id,
            "event_statut": False,
            "attendees": 84,
            "event_date": "2023-03-29T13:34:00.00Z",
            "notes": "notes 4",
            "contract_id": create_contract.id,
        }
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.put(f"/events/{event_object.id}/", payload)

        assert response.status_code == 403
        assert b"You do not have permission to perform this action." in response.content
