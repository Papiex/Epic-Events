import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from contracts.models import Contract
from customers.models import Customer


pytestmark = pytest.mark.django_db


@pytest.fixture
def create_other_customer(saler_user):
    customer = Customer.objects.create(
            first_name = 'test',
            last_name = 'othertest',
            email = 'othertest@mail.fr',
            phone = '0622395894',
            mobile = '0622395894',
            company_name = 'test',
            customer_type = 'POTENTIAL',
            sales_contact_id = saler_user
            )
    return customer


@pytest.fixture
def payload_01(saler_user, create_customer):
    """return data for contract object"""
    return {
            'sales_contact_id': saler_user,
            'customer_id': create_customer,
            'status': 'False',
            'amount': '25.80',
            'payment_due': '2023-03-29T13:34:00.000',
        }


@pytest.fixture
def payload_02(saler_user, create_other_customer):
    """return data with different value for contract object"""
    return {
            'sales_contact_id': saler_user,
            'customer_id': create_other_customer,
            'status': 'False',
            'amount': '32',
            'payment_due': '2025-03-29T13:34:00.000',
        }


class TestFilters:

    def test_should_return_five_results_with_email(self, api_client, saler_user, payload_01, payload_02):
        """create 5 same contracts and 5 other with different customer mail"""
        for i in range(5):
            Contract.objects.create(**payload_01)
            Contract.objects.create(**payload_02)
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.get('/contracts/?customer_id__email=test@mail.fr')

        assert response.status_code == 200
        assert len(response.data) == 5


    def test_should_return_five_results_with_last_name(self, api_client, saler_user, payload_01, payload_02):
        """create 5 same contracts and 5 other with different customer last_name"""
        for i in range(5):
            Contract.objects.create(**payload_01)
            Contract.objects.create(**payload_02)
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.get('/contracts/?customer_id__last_name=test')

        assert response.status_code == 200
        assert len(response.data) == 5
    

    def test_should_return_five_results_with_amount(self, api_client, saler_user, payload_01, payload_02):
        """create 5 same contracts and 5 other with different amount"""
        for i in range(5):
            Contract.objects.create(**payload_01)
            Contract.objects.create(**payload_02)
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.get('/contracts/?amount=25.80')

        assert response.status_code == 200
        assert len(response.data) == 5


    def test_should_return_five_results_with_date_created(self, api_client, saler_user, payload_01, payload_02):
        """create 5 same contracts and 5 other with different date"""
        for i in range(5):
            Contract.objects.create(**payload_01)
            Contract.objects.create(**payload_02)
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.get('/contracts/?payment_due=2023-03-29T13:34:00.000')

        assert response.status_code == 200
        assert len(response.data) == 5
