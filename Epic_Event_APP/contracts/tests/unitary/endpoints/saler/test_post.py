import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from contracts.models import Contract
from users.models import User


pytestmark = pytest.mark.django_db


class TestPostEndpoint:
    def test_should_post(self, api_client, create_customer, saler_user):
        """test post with saler_user"""
        payload = {
            "sales_contact_id": saler_user,
            "customer_id": create_customer.id,
            "amount": 17.96,
            "status": True,
            "payment_due": "2023-03-29T13:34:00.000",
        }
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.post("/contracts/", payload)
        data = response.data

        contract_db = Contract.objects.all().first()

        assert response.status_code == 201
        assert len(Contract.objects.all()) == 1
        assert data["sales_contact_id"] == contract_db.sales_contact_id.id
        assert data["customer_id"] == contract_db.customer_id.id
        assert data["status"] == contract_db.status
        assert data["amount"] == contract_db.amount
        assert data["payment_due"] == "2023-03-29T13:34:00Z"

    def test_should_not_post(self, api_client, create_customer, saler_user):
        """test post with customer rattached to another saler user"""
        other_saler_user = User.objects.create(
            username="other_saler", password="motdepasse78"
        )
        payload = {
            "sales_contact_id": saler_user,
            "customer_id": create_customer.id,
            "amount": 17.96,
            "status": True,
            "payment_due": "2023-03-29T13:34:00.000",
        }
        refresh = RefreshToken.for_user(other_saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.post("/contracts/", payload)

        assert response.status_code == 403
        assert b"You do not have permission to perform this action." in response.content
