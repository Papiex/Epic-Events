import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from contracts.models import Contract


pytestmark = pytest.mark.django_db


class TestGetEndpoint:
    def test_should_get_list(self, api_client, create_customer, saler_user):
        """test get list with saler_user"""
        payload = {
            "sales_contact_id": saler_user,
            "customer_id": create_customer,
            "status": "False",
            "amount": "25.80",
            "payment_due": "2023-03-29T13:34:00.000",
        }
        Contract.objects.create(**payload)
        Contract.objects.create(**payload)
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.get(f"/contracts/")

        assert response.status_code == 200
        assert len(Contract.objects.all()) == 2

    def test_should_get_detail(self, api_client, saler_user, create_contract):
        """test get detail with saler_user"""
        contract_object = create_contract
        contract_db = Contract.objects.all().first()
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.get(f"/contracts/{contract_object.id}/")
        data = response.data

        assert response.status_code == 200
        assert data["sales_contact_id"] == contract_db.sales_contact_id.id
        assert data["customer_id"] == contract_db.customer_id.id
        assert data["status"] == contract_db.status
        assert data["amount"] == contract_db.amount
        assert data["payment_due"] == "2023-03-29T13:34:00Z"
