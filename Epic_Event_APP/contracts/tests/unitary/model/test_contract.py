import pytest

from contracts.models import Contract
from users.models import User
from customers.models import Customer


pytestmark = pytest.mark.django_db


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


class TestContractModel:
    def test_should_create_contract(
        self, create_contract, create_customer, create_user
    ):
        """test creating contract"""
        contract = create_contract
        assert contract.sales_contact_id == create_user
        assert contract.customer_id == create_customer
        assert contract.status == True
        assert contract.amount == 125.96
        assert contract.payment_due == "2023-03-29T13:34:00.000"

    def test_should_get_contract(self, create_contract):
        """test get contract"""
        contract = create_contract
        get_contract = Contract.objects.all().first()

        assert contract.sales_contact_id == get_contract.sales_contact_id
        assert contract.customer_id == get_contract.customer_id
        assert contract.status == get_contract.status
        assert contract.amount == get_contract.amount
        assert contract.payment_due == "2023-03-29T13:34:00.000"

    def test_should_update_contract(self, create_contract):
        """test updating contract"""
        contract = create_contract
        contract.amount = 250.87
        contract.status = False
        contract.payment_due = "2024-03-29T13:34:00.000"

        assert contract.amount == 250.87
        assert contract.status == False
        assert contract.payment_due == "2024-03-29T13:34:00.000"

    def test_should_delete_contract(self, create_contract):
        """test deleting contract"""
        contract = create_contract
        contract.delete()

        assert len(Contract.objects.all()) == 0
