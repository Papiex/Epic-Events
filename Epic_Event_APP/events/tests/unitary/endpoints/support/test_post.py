import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from events.models import Event
from users.models import User


pytestmark = pytest.mark.django_db


class TestPostEndpoint:
    def test_should_not_post(self, api_client, support_user, create_contract):
        """test post with support user."""
        payload = {
            "support_contact_id": support_user.id,
            "event_statut": True,
            "attendees": 42,
            "event_date": "2023-03-29T13:34:00.00Z",
            "notes": "notes",
            "contract_id": create_contract.id,
        }
        refresh = RefreshToken.for_user(support_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.post("/events/", payload)

        assert response.status_code == 403
        assert b"You do not have permission to perform this action." in response.content
