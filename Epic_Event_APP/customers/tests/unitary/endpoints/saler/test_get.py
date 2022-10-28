import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from customers.models import Customer


pytestmark = pytest.mark.django_db


class TestGetEndpoint:

    def test_should_get_list(self, api_client, saler_user):
        """test get list of customers objects with saler user"""
        payload = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@mail.fr',
            'phone': '0622395894',
            'mobile': '0622395894',
            'company_name': 'test',
            'customer_type': 'POTENTIAL',
            'sales_contact_id': saler_user
        }
        Customer.objects.create(**payload)
        Customer.objects.create(**payload)

        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.get('/customers/')

        assert response.status_code == 200
        assert len(response.data) == 2
    

    def test_should_get_detail(self, api_client, saler_user, create_customer):
        """test get detail of customer object with saler user"""
        customer_object = create_customer
        customer_db = Customer.objects.all().first()
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.get(f'/customers/{customer_object.id}/')
        data = response.data

        assert response.status_code == 200
        assert data['first_name'] == customer_db.first_name
        assert data['last_name'] == customer_db.last_name
        assert data['email'] == customer_db.email
        assert data['phone'] == customer_db.phone
        assert data['mobile'] == customer_db.mobile
        assert data['company_name'] == customer_db.company_name
        assert data['customer_type'] == customer_db.customer_type
        assert data['sales_contact_id'] == customer_db.sales_contact_id.id
