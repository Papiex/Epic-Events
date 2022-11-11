from rest_framework.test import APIClient

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

import pytest

from users.models import User
from customers.models import Customer
from contracts.models import Contract
from events.models import Event


@pytest.fixture
def create_customer(saler_user) -> Customer:
    """create and return customer"""
    customer = Customer.objects.create(
        first_name="test",
        last_name="test",
        email="test@mail.fr",
        phone="0622395894",
        mobile="0622395894",
        company_name="test",
        customer_type="POTENTIAL",
        sales_contact_id=saler_user,
    )
    return customer


@pytest.fixture
def api_client() -> APIClient:
    client = APIClient()

    return client


@pytest.fixture
def saler_user() -> User:
    """ """
    saler_group = create_and_get_permissions_for_saler_group()

    user = User.objects.create(
        role="SALER",
        username="saler_user_testing",
        first_name="saler_user_testing",
        last_name="saler_user_testing",
        email="saler_user@mail.fr",
    )
    user.groups.add(saler_group)
    user.set_password("motdepasse78")

    return user


@pytest.fixture
def support_user() -> User:
    """ """
    support_group = create_and_get_permissions_for_support_group()

    user = User.objects.create(
        role="SUPPORT",
        username="support_user_testing",
        first_name="support_user_testing",
        last_name="support_user_testing",
        email="support_user@mail.fr",
    )
    user.groups.add(support_group)
    user.set_password("motdepasse78")

    return user


@pytest.fixture
def gestion_user() -> User:
    """ """
    gestion_group = create_and_get_permissions_for_gestion_group()

    user = User.objects.create(
        role="GESTION",
        username="gestion_user_testing",
        first_name="gestion_user_testing",
        last_name="gestion_user_testing",
        email="gestion_user@mail.fr",
    )
    user.groups.add(gestion_group)
    user.set_password("motdepasse78")

    return user


def create_and_get_permissions_for_support_group() -> Group:
    """Create support group and fill it with correct permission"""
    support_group = Group.objects.create(name="Support Team")
    content_type = ContentType.objects.get_for_model(Contract)
    contract_permission = Permission.objects.filter(content_type=content_type).get(
        name="Can view contract"
    )
    support_group.permissions.add(contract_permission)

    content_type = ContentType.objects.get_for_model(Customer)
    customer_permission = Permission.objects.filter(content_type=content_type).get(
        name="Can view customer"
    )
    support_group.permissions.add(customer_permission)

    content_type = ContentType.objects.get_for_model(Event)
    event_permissions = (
        Permission.objects.filter(content_type=content_type)
        .exclude(name="Can add event")
        .exclude(name="Can delete event")
    )

    for permission in event_permissions:
        support_group.permissions.add(permission)

    return support_group


def create_and_get_permissions_for_saler_group() -> Group:
    """Create saler group and fill it with correct permission"""
    saler_group = Group.objects.create(name="Saler Team")
    content_type = ContentType.objects.get_for_model(Customer)
    customer_permissions = Permission.objects.filter(content_type=content_type)

    for permission in customer_permissions:
        saler_group.permissions.add(permission)

    content_type = ContentType.objects.get_for_model(Contract)
    contract_permissions = Permission.objects.filter(content_type=content_type).exclude(
        name="Can delete contract"
    )

    for permission in contract_permissions:
        saler_group.permissions.add(permission)

    content_type = ContentType.objects.get_for_model(Event)
    event_permissions = Permission.objects.filter(content_type=content_type).exclude(
        name="Can delete event"
    )

    for permission in event_permissions:
        saler_group.permissions.add(permission)

    return saler_group


def create_and_get_permissions_for_gestion_group() -> Group:
    """Create gestion group and fill it with correct permission"""
    gestion_group = Group.objects.create(name="Gestion Team")
    content_type = ContentType.objects.get_for_model(Customer)
    customer_permission = Permission.objects.filter(content_type=content_type)

    for permission in customer_permission:
        gestion_group.permissions.add(permission)

    content_type = ContentType.objects.get_for_model(Event)
    event_permissions = Permission.objects.filter(content_type=content_type)

    for permission in event_permissions:
        gestion_group.permissions.add(permission)

    content_type = ContentType.objects.get_for_model(Contract)
    contract_permissions = Permission.objects.filter(content_type=content_type)

    for permission in contract_permissions:
        gestion_group.permissions.add(permission)

    content_type = ContentType.objects.get_for_model(User)
    user_permissions = Permission.objects.filter(content_type=content_type)

    for permission in user_permissions:
        gestion_group.permissions.add(permission)

    return gestion_group
