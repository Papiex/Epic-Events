import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from customers.models import Customer


pytestmark = pytest.mark.django_db


class TestPostEndPoint:


    def test_should_post(self, api_client, saler_user):
        """test post request with saler user"""
        payload = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@mail.fr',
            'phone': '0622395894',
            'mobile': '0622395894',
            'company_name': 'test',
            'customer_type': 'POTENTIAL',
        }
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.post('/customers/', payload)
        data = response.data

        customer_db = Customer.objects.all().first()

        assert response.status_code == 201
        assert data['first_name'] == customer_db.first_name
        assert data['last_name'] == customer_db.last_name
        assert data['email'] == customer_db.email
        assert data['phone'] == customer_db.phone
        assert data['mobile'] == customer_db.mobile
        assert data['company_name'] == customer_db.company_name
        assert data['customer_type'] == customer_db.customer_type
        assert data['sales_contact_id'] == customer_db.sales_contact_id.id
