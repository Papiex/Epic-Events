import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from contracts.models import Contract


pytestmark = pytest.mark.django_db


class TestDeleteEndpoint:
    def test_should_not_delete(self, api_client, saler_user, create_contract):
        """test deleting with saler_user"""
        contract_object = create_contract

        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.delete(f"/contracts/{contract_object.id}/")

        assert response.status_code == 403
        assert b"You do not have permission to perform this action." in response.content
