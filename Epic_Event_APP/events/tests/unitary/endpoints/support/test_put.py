import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from events.models import Event
from users.models import User


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
        refresh = RefreshToken.for_user(support_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.put(f"/events/{event_object.id}/", payload)
        data = response.data

        event_db = Event.objects.all().first()

        assert response.status_code == 200
        assert data["support_contact_id"] == event_db.support_contact_id.id
        assert data["event_statut"] == event_db.event_statut
        assert data["attendees"] == event_db.attendees
        assert data["event_date"] == "2023-03-29T13:34:00Z"
        assert data["notes"] == event_db.notes
        assert data["contract_id"] == event_db.contract_id.id

    def test_should_not_update(
        self, create_contract, create_event, api_client, support_user
    ):
        """test with other support user attached to the event"""
        other_support_user = User.objects.create(
            username="other_support", password="motdepasse78", role="SUPPORT"
        )
        event_object = create_event
        payload = {
            "support_contact_id": support_user.id,
            "event_statut": False,
            "attendees": 84,
            "event_date": "2023-03-29T13:34:00.00Z",
            "notes": "notes 4",
            "contract_id": create_contract.id,
        }
        refresh = RefreshToken.for_user(other_support_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.put(f"/events/{event_object.id}/", payload)

        assert response.status_code == 403
        assert b"You do not have permission to perform this action." in response.content
