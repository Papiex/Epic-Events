import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from customers.models import Customer


pytestmark = pytest.mark.django_db


class TestDeleteEndpoint:

    def test_should_not_delete(self, api_client, saler_user, support_user, create_customer):
        """test deleting with saler_user"""
        customer_object = create_customer

        refresh = RefreshToken.for_user(support_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.delete(f'/customers/{customer_object.id}/')

        assert response.status_code == 403
        assert b"You do not have permission to perform this action." in response.content
        assert len(Customer.objects.all()) == 1