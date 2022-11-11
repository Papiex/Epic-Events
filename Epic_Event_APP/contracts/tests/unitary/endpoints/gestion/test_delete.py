import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from contracts.models import Contract


pytestmark = pytest.mark.django_db


class TestDeleteEndpoint:
    def test_should_delete(self, api_client, gestion_user, create_contract):
        """test deleting with gestion_user"""
        contract_object = create_contract

        refresh = RefreshToken.for_user(gestion_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.delete(f"/contracts/{contract_object.id}/")

        assert response.status_code == 204
        assert len(Contract.objects.all()) == 0
