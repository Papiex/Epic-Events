import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from customers.models import Customer
from users.models import User


pytestmark = pytest.mark.django_db


class TestPutEndpoint:
    def test_should_not_update(self, api_client, saler_user, support_user):
        """test updating customer with a support user"""
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

        refresh = RefreshToken.for_user(support_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

        updated_payload = {
            "first_name": "update_test",
            "last_name": "update_test",
        }
        response = api_client.put(f"/customers/{customer_object.id}/", updated_payload)

        assert response.status_code == 403
        assert b"You do not have permission to perform this action." in response.content
