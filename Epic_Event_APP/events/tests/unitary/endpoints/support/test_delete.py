import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from events.models import Event


pytestmark = pytest.mark.django_db


class TestDeleteEndpoint:
    def test_should_not_delete(self, api_client, support_user, create_event):
        """test deleting with support_user"""
        event_object = create_event

        refresh = RefreshToken.for_user(support_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.delete(f"/events/{event_object.id}/")

        assert response.status_code == 403
        assert b"You do not have permission to perform this action." in response.content
