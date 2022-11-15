import pytest

from rest_framework_simplejwt.tokens import RefreshToken

from contracts.models import Contract
from customers.models import Customer
from events.models import Event


pytestmark = pytest.mark.django_db


@pytest.fixture
def create_contracts(saler_user, create_customer) -> Contract:
    """return multiple contracts with different ids"""
    payload = {
        "sales_contact_id": saler_user,
        "customer_id": create_customer,
        "status": "False",
        "amount": "25.80",
        "payment_due": "2023-03-29T13:34:00.000",
    }
    contrat_01 = Contract.objects.create(**payload)
    contrat_02 = Contract.objects.create(**payload)
    contrat_03 = Contract.objects.create(**payload)
    contrat_04 = Contract.objects.create(**payload)

    return contrat_01, contrat_02, contrat_03, contrat_04


@pytest.fixture
def create_other_customer(saler_user) -> Customer:
    customer = Customer.objects.create(
        first_name="test",
        last_name="othertest",
        email="othertest@mail.fr",
        phone="0622395894",
        mobile="0622395894",
        company_name="test",
        customer_type="POTENTIAL",
        sales_contact_id=saler_user,
    )
    return customer


@pytest.fixture
def payload_01(saler_user, create_customer, create_contracts) -> dict:
    event_with_contract_01 = {
        "customer_id": create_customer,
        "support_contact_id": saler_user,
        "event_statut": True,
        "attendees": 42,
        "event_date": "2025-03-29T13:34:00.00Z",
        "notes": "notes",
        "contract_id": create_contracts[0],
    }
    event_with_contract_02 = {
        "customer_id": create_customer,
        "support_contact_id": saler_user,
        "event_statut": True,
        "attendees": 42,
        "event_date": "2025-03-29T13:34:00.00Z",
        "notes": "notes",
        "contract_id": create_contracts[1],
    }
    return event_with_contract_01, event_with_contract_02


@pytest.fixture
def payload_02(saler_user, create_other_customer, create_contracts) -> dict:
    event_with_contract_03 = {
        "customer_id": create_other_customer,
        "support_contact_id": saler_user,
        "event_statut": True,
        "attendees": 42,
        "event_date": "2027-03-29T13:34:00.00Z",
        "notes": "notes",
        "contract_id": create_contracts[2],
    }
    event_with_contract_04 = {
        "customer_id": create_other_customer,
        "support_contact_id": saler_user,
        "event_statut": True,
        "attendees": 42,
        "event_date": "2027-03-29T13:34:00.00Z",
        "notes": "notes",
        "contract_id": create_contracts[3],
    }
    return event_with_contract_03, event_with_contract_04


class TestFilters:
    def test_should_return_two_results_with_email(
        self, saler_user, api_client, payload_01, payload_02
    ):
        """create 2 same events and 2 other with different customer mail"""
        Event.objects.create(**payload_01[0])
        Event.objects.create(**payload_01[1])
        Event.objects.create(**payload_02[0])
        Event.objects.create(**payload_02[1])
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.get("/events/?email=test@mail.fr")

        assert response.status_code == 200
        assert len(response.data) == 2

    def test_should_return_two_results_with_last_name(
        self, saler_user, api_client, payload_01, payload_02
    ):
        """create 2 same events and 2 other with different customer last name"""
        Event.objects.create(**payload_01[0])
        Event.objects.create(**payload_01[1])
        Event.objects.create(**payload_02[0])
        Event.objects.create(**payload_02[1])
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.get("/events/?last_name=test")

        assert response.status_code == 200
        assert len(response.data) == 2

    def test_should_return_two_results_with_date(
        self, saler_user, api_client, payload_01, payload_02
    ):
        """create 2 same events and 2 other with different event date"""
        Event.objects.create(**payload_01[0])
        Event.objects.create(**payload_01[1])
        Event.objects.create(**payload_02[0])
        Event.objects.create(**payload_02[1])
        refresh = RefreshToken.for_user(saler_user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.get("/events/?event_date=2025-03-29T13:34:00.00Z")

        assert response.status_code == 200
        assert len(response.data) == 2
