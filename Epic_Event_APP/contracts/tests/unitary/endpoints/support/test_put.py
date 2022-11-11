import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from contracts.models import Contract
from users.models import User


pytestmark = pytest.mark.django_db


class TestPutEndpoint:
    def test_should_not_put(
        self, create_contract, api_client, create_customer, saler_user, support_user
    ):
        """test put with support_user"""
        contract_object = create_contract
        payload = {
            "sales_contact_id": saler_user,
            "customer_id": create_customer.id,
            "status": "False",
            "amount": "25.80",
            "payment_due": "2023-03-29T13:34:00.000",
        }
        refresh = RefreshToken.for_user(support_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.put(f"/contracts/{contract_object.id}/", payload)

        assert response.status_code == 403
        assert b"You do not have permission to perform this action." in response.content
