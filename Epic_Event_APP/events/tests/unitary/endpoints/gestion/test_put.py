import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from contracts.models import Contract
from events.models import Event


pytestmark = pytest.mark.django_db


class TestPutEndpoint:

    def test_should_update(self, create_contract, create_event, gestion_user, api_client, support_user):
        """test update with gestion_user"""
        event_object = create_event
        payload = {
            'support_contact_id': support_user.id,
            'event_statut': False,
            'attendees': 84,
            'event_date': '2023-03-29T13:34:00.00Z',
            'notes': 'notes 4',
            'contract_id': create_contract.id
        }
        refresh = RefreshToken.for_user(gestion_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.put(f'/events/{event_object.id}/', payload)
        data = response.data

        event_db = Event.objects.all().first()

        assert response.status_code == 200
        assert data['support_contact_id'] == event_db.support_contact_id.id
        assert data['event_statut'] == event_db.event_statut
        assert data['attendees'] == event_db.attendees
        assert data['event_date'] == '2023-03-29T13:34:00Z'
        assert data['notes'] == event_db.notes
        assert data['contract_id'] == event_db.contract_id.id
