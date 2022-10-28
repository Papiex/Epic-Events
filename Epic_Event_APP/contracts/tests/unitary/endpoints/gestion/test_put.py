import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from contracts.models import Contract


pytestmark = pytest.mark.django_db


class TestPutEndpoint:

    def test_should_update(self, create_contract, gestion_user, api_client, create_customer, saler_user):
        """test update with gestion_user"""
        contract_object = create_contract
        payload = {
            'sales_contact_id': saler_user,
            'customer_id': create_customer.id,
            'status': 'False',
            'amount': '25.80',
            'payment_due': '2023-03-29T13:34:00.000',
        }
        refresh = RefreshToken.for_user(gestion_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.put(f'/contracts/{contract_object.id}/', payload)
        data = response.data

        contract_db = Contract.objects.all().first()

        assert response.status_code == 200
        assert data['sales_contact_id'] == contract_db.sales_contact_id.id
        assert data['customer_id'] == contract_db.customer_id.id
        assert data['status'] == contract_db.status
        assert data['amount'] == contract_db.amount
        assert data['payment_due'] == '2023-03-29T13:34:00Z'
