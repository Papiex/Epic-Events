import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from customers.models import Customer


pytestmark = pytest.mark.django_db


class TestPutEndpoint:
    def test_should_update(self, api_client, gestion_user):
        """test updating with gestion user"""
        payload = {
            "first_name": "test",
            "last_name": "test",
            "email": "test@mail.fr",
            "phone": "0622395894",
            "mobile": "0622395894",
            "company_name": "test",
            "customer_type": "POTENTIAL",
            "sales_contact_id": gestion_user,
        }
        customer_object = Customer.objects.create(**payload)
        refresh = RefreshToken.for_user(gestion_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        updated_payload = {
            "first_name": "update_test",
            "last_name": "update_test",
            "email": "test@mail.fr",
            "phone": "0622395894",
            "mobile": "0622395894",
            "company_name": "test",
            "customer_type": "EXISTING",
        }
        response = api_client.put(f"/customers/{customer_object.id}/", updated_payload)
        data = response.data
        customer_object = Customer.objects.all().first()

        assert response.status_code == 200
        assert data["first_name"] == customer_object.first_name
        assert data["last_name"] == customer_object.last_name

    def test_should_update_even_if_not_owner(
        self, api_client, create_customer, gestion_user
    ):
        """test updating customer created with a saler user"""
        customer_object = create_customer
        refresh = RefreshToken.for_user(gestion_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        updated_payload = {
            "first_name": "update_test",
            "last_name": "update_test",
            "email": "test@mail.fr",
            "phone": "0622395894",
            "mobile": "0622395894",
            "company_name": "test",
            "customer_type": "EXISTING",
        }
        response = api_client.put(f"/customers/{customer_object.id}/", updated_payload)
        data = response.data
        customer_object = Customer.objects.all().first()

        assert response.status_code == 200
        assert data["first_name"] == customer_object.first_name
        assert data["last_name"] == customer_object.last_name
