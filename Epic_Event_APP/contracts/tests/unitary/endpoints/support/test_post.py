import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from contracts.models import Contract


pytestmark = pytest.mark.django_db


class TestPostEndpoint:
    def test_should_post(self, api_client, create_customer, support_user):
        """test post with support_user"""
        payload = {
            "sales_contact_id": support_user,
            "customer_id": create_customer.id,
            "amount": 17.96,
            "status": True,
            "payment_due": "2023-03-29T13:34:00.000",
        }
        refresh = RefreshToken.for_user(support_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.post("/contracts/", payload)

        assert response.status_code == 403
        assert b"You do not have permission to perform this action." in response.content
