import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from customers.models import Customer


pytestmark = pytest.mark.django_db


class TestDeleteEndpoint:

    def test_should_delete(self, api_client, gestion_user, create_customer):
        """test deleting with saler_user"""
        customer_object = create_customer

        refresh = RefreshToken.for_user(gestion_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.delete(f'/customers/{customer_object.id}/')

        assert response.status_code == 204
        assert len(Customer.objects.all()) == 0