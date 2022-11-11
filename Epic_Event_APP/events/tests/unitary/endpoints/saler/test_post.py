import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from events.models import Event
from users.models import User


pytestmark = pytest.mark.django_db


class TestPostEndpoint:
    def test_should_post(self, api_client, saler_user, support_user, create_contract):
        """test post with gestion_user"""
        payload = {
            "support_contact_id": support_user.id,
            "event_statut": True,
            "attendees": 42,
            "event_date": "2023-03-29T13:34:00.00Z",
            "notes": "notes",
            "contract_id": create_contract.id,
        }
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.post("/events/", payload)
        data = response.data

        event_db = Event.objects.all().first()

        assert response.status_code == 201
        assert len(Event.objects.all()) == 1
        assert data["customer_id"] == event_db.customer_id.id
        assert data["event_statut"] == event_db.event_statut
        assert data["attendees"] == event_db.attendees
        assert data["event_date"] == "2023-03-29T13:34:00Z"
        assert data["notes"] == event_db.notes
        assert data["contract_id"] == event_db.contract_id.id

    def test_should_not_post(self, api_client, support_user, create_contract):
        """test post with other saler user rattached to contracts."""
        other_saler_user = User.objects.create(
            username="other_saler", password="motdepasse78"
        )
        payload = {
            "support_contact_id": support_user.id,
            "event_statut": True,
            "attendees": 42,
            "event_date": "2023-03-29T13:34:00.00Z",
            "notes": "notes",
            "contract_id": create_contract.id,
        }
        refresh = RefreshToken.for_user(other_saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.post("/events/", payload)

        assert response.status_code == 403
        assert b"You do not have permission to perform this action." in response.content
