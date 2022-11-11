import pytest

from contracts.models import Contract
from users.models import User
from customers.models import Customer
from events.models import Event


pytestmark = pytest.mark.django_db


@pytest.fixture
def create_event(create_customer, create_user, create_contract):
    event = Event.objects.create(
        customer_id=create_customer,
        support_contact_id=create_user,
        event_statut=True,
        attendees=59,
        event_date="2023-03-29T13:34:00.000",
        notes="test notes",
        contract_id=create_contract,
    )
    return event


@pytest.fixture
def create_contract(create_user, create_customer):
    contract = Contract.objects.create(
        sales_contact_id=create_user,
        customer_id=create_customer,
        status=True,
        amount=125.96,
        payment_due="2023-03-29T13:34:00.000",
    )
    return contract


@pytest.fixture
def create_customer(create_user):
    customer = Customer.objects.create(
        first_name="test_customer",
        last_name="test_customer",
        email="test@customer.test",
        phone="0625898747",
        mobile="0625898747",
        company_name="test_company_customer",
        sales_contact_id=create_user,
        customer_type="POTENTIAL",
    )
    return customer


@pytest.fixture
def create_user():
    user = User.objects.create()
    return user


class TestEventModel:
    def test_should_create_event(
        self, create_customer, create_contract, create_event, create_user
    ):
        """test creating event"""
        event = create_event

        assert event.customer_id == create_customer
        assert event.support_contact_id == create_user
        assert event.event_statut == True
        assert event.attendees == 59
        assert event.event_date == "2023-03-29T13:34:00.000"
        assert event.notes == "test notes"
        assert event.contract_id == create_contract

    def test_should_get_event(self, create_event):
        """test get event"""
        event = create_event
        get_event = Event.objects.all().first()

        assert event.customer_id == get_event.customer_id
        assert event.support_contact_id == get_event.support_contact_id
        assert event.attendees == get_event.attendees
        assert event.event_date == "2023-03-29T13:34:00.000"
        assert event.notes == get_event.notes
        assert event.contract_id == get_event.contract_id
        assert event.event_statut == get_event.event_statut

    def test_should_update_event(self, create_event):
        """test updating event"""
        event = create_event

        event.event_statut = False
        event.event_date = "2024-03-29T13:34:00.000"
        event.notes = "updated notes"
        event.attendees = 65

        assert event.event_statut == False
        assert event.notes == "updated notes"
        assert event.attendees == 65
        assert event.event_date == "2024-03-29T13:34:00.000"

    def test_should_delete_event(self, create_event):
        """test deleting event"""
        event = create_event
        event.delete()

        assert len(Event.objects.all()) == 0
