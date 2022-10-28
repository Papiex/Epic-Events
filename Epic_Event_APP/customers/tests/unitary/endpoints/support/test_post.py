import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from customers.models import Customer


pytestmark = pytest.mark.django_db


class TestPostEndPoint:


    def test_should_not_post(self, api_client, support_user):
        """test post request with support user"""
        payload = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@mail.fr',
            'phone': '0622395894',
            'mobile': '0622395894',
            'company_name': 'test',
            'customer_type': 'POTENTIAL',
        }
        refresh = RefreshToken.for_user(support_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.post('/customers/', payload)

        assert response.status_code == 403
        assert b"You do not have permission to perform this action." in response.content
        assert len(Customer.objects.all()) == 0
