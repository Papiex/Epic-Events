import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from customers.models import Customer


pytestmark = pytest.mark.django_db


class TestDeleteEndpoint:
    def test_should_not_delete(self, api_client, saler_user):
        """test deleting with saler_user"""
        payload = {
            "first_name": "test",
            "last_name": "test",
            "email": "test@mail.fr",
            "phone": "0622395894",
            "mobile": "0622395894",
            "company_name": "test",
            "customer_type": "POTENTIAL",
            "sales_contact_id": saler_user,
        }
        customer_object = Customer.objects.create(**payload)

        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.delete(f"/customers/{customer_object.id}/")

        assert response.status_code == 403
        assert b"You do not have permission to perform this action." in response.content
        assert len(Customer.objects.all()) == 1
