import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from customers.models import Customer


pytestmark = pytest.mark.django_db


class TestFilters:

    def test_should_return_five_results_with_email(self, api_client, saler_user):
        """create 5 same customer and 5 other with different mail and get the same email"""
        payload_01 = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@mail.fr',
            'phone': '0622395894',
            'mobile': '0622395894',
            'company_name': 'test',
            'customer_type': 'POTENTIAL',
            'sales_contact_id': saler_user
        }
        payload_02 = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'othertest@mail.fr',
            'phone': '0622395894',
            'mobile': '0622395894',
            'company_name': 'test',
            'customer_type': 'POTENTIAL',
            'sales_contact_id': saler_user
        }
        for i in range(5):
            Customer.objects.create(**payload_01)
            Customer.objects.create(**payload_02)
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.get('/customers/?email=test@mail.fr')

        assert response.status_code == 200
        assert len(response.data) == 5


    def test_should_return_five_results_with_last_name(self, api_client, saler_user):
        """create 5 same customer and 5 other with different last name and get the same last name"""
        payload_01 = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@mail.fr',
            'phone': '0622395894',
            'mobile': '0622395894',
            'company_name': 'test',
            'customer_type': 'POTENTIAL',
            'sales_contact_id': saler_user
        }
        payload_02 = {
            'first_name': 'test',
            'last_name': 'othertest',
            'email': 'othertest@mail.fr',
            'phone': '0622395894',
            'mobile': '0622395894',
            'company_name': 'test',
            'customer_type': 'POTENTIAL',
            'sales_contact_id': saler_user
        }
        for i in range(5):
            Customer.objects.create(**payload_01)
            Customer.objects.create(**payload_02)
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.get('/customers/?last_name=test')

        assert response.status_code == 200
        assert len(response.data) == 5
