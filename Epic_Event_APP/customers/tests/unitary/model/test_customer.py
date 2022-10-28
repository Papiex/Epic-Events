import pytest

from customers.models import Customer
from users.models import User


pytestmark = pytest.mark.django_db


@pytest.fixture   
def create_customer(create_user):
    customer = Customer.objects.create(
        first_name = 'test_customer',
        last_name = 'test_customer',
        email = 'test@customer.test',
        phone = '0625898747',
        mobile = '0625898747',
        company_name = 'test_company_customer',
        sales_contact_id = create_user,
        customer_type = 'POTENTIAL',
    )
    return customer


@pytest.fixture
def create_user():
    user = User.objects.create()
    return user


class TestCustomerModel:

    def test_should_create_customer(self, create_customer, create_user):
        """test creating customer"""
        customer = create_customer

        assert customer.first_name == 'test_customer'
        assert customer.last_name == 'test_customer'
        assert customer.email == 'test@customer.test'
        assert customer.phone == '0625898747'
        assert customer.mobile == '0625898747'
        assert customer.company_name == 'test_company_customer'
        assert customer.sales_contact_id == create_user
        assert customer.customer_type == 'POTENTIAL'


    def test_should_get_customer(self, create_customer):
        """test get customer"""
        customer = create_customer
        get_customer = Customer.objects.all().first()

        assert customer.first_name == get_customer.first_name
        assert customer.last_name == get_customer.last_name
        assert customer.email == get_customer.email
        assert customer.phone == get_customer.phone
        assert customer.mobile == get_customer.mobile
        assert customer.company_name == get_customer.company_name
        assert customer.sales_contact_id == get_customer.sales_contact_id


    def test_should_update_customer(self, create_customer):
        """test updating customer"""
        customer = create_customer

        customer.customer_type = 'EXISTING'
        customer.email = 'testupdate@customer.test'
        customer.first_name = 'update first name'
        customer.last_name = 'update last name'
        customer.mobile = '0636987847'
        customer.phone = '0636987847'

        assert customer.customer_type == 'EXISTING'
        assert customer.email == 'testupdate@customer.test'
        assert customer.first_name == 'update first name'
        assert customer.last_name == 'update last name'
        assert customer.mobile == '0636987847'
        assert customer.phone == '0636987847'


    def test_should_delete_customer(self):
        """test deleting customer"""
        customer = Customer.objects.create()
        customer.delete()

        assert len(Customer.objects.all()) == 0
