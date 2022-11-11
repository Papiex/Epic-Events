from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from datetime import datetime
import pytz

from customers.models import Customer
from contracts.models import Contract


class EventPermission(BasePermission):
    """
    Allow gestion, saler, support users to get and list all customers
    Allow only the assigned support_contact to modify the object
    Allow all with gestion user
    """

    def has_permission(self, request, view) -> bool:

        if request.method == "GET":
            return (
                request.user.role == "SUPPORT"
                or request.user.role == "SALER"
                or request.user.role == "GESTION"
            )
        if request.method == "DELETE":
            return request.user.role == "GESTION"
        if request.method == "POST":
            contract = get_object_or_404(Contract, id=request.data.get("contract_id"))
            customer = get_object_or_404(Customer, id=contract.customer_id.id)
            return (
                customer.sales_contact_id == request.user
                and contract.sales_contact_id == request.user
                and request.user.role == "SALER"
                or request.user.role == "GESTION"
            )
        if request.method == "PUT" or request.method == "PATCH":
            return True

    def has_object_permission(self, request, view, obj) -> bool:
        utc = pytz.UTC
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "DELETE":
            return request.user.role == "GESTION"
        if request.method == "PUT" or request.method == "PATCH":
            if request.user.role == "GESTION":
                return True
            elif obj.event_date.replace(tzinfo=utc) < datetime.now().replace(
                tzinfo=utc
            ):
                return False
            else:
                return (
                    request.user == obj.support_contact_id
                    and request.user.role == "SUPPORT"
                    or request.user.role == "GESTION"
                )
