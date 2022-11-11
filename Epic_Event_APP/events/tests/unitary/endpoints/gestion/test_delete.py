import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from events.models import Event


pytestmark = pytest.mark.django_db


class TestDeleteEndpoint:
    def test_should_delete(self, api_client, gestion_user, create_event):
        """test deleting with gestion_user"""
        event_object = create_event

        refresh = RefreshToken.for_user(gestion_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.delete(f"/events/{event_object.id}/")

        assert response.status_code == 204
        assert len(Event.objects.all()) == 0
