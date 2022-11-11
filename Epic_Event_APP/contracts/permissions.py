from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from customers.models import Customer


class ContractPermission(BasePermission):
    """
    Allow gestion, saler, support users to get and list all customers
    Does not allow delete for saler and support users
    Allow only owner to update the customer
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
            customer = get_object_or_404(Customer, id=request.data.get("customer_id"))
            return (
                customer.sales_contact_id == request.user
                and request.user.role == "SALER"
                or request.user.role == "GESTION"
            )
        if request.method == "PUT" or request.method == "PATCH":
            return True

    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "DELETE":
            return request.user.role == "GESTION"
        if request.method == "PUT" or request.method == "PATCH":
            if request.user.role == "GESTION":
                return True
            else:
                return (
                    request.user == obj.customer_id.sales_contact_id
                    and request.user == obj.sales_contact_id
                    and request.user.role == "SALER"
                )
