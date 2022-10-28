from rest_framework.permissions import BasePermission
from rest_framework import permissions


class CustomerPermission(BasePermission):
    """
    Allow gestion, saler, support users to get and list all customers
    Does not allow delete for saler and support users
    Allow only owner to update the customer 
    """

    def has_permission(self, request, view) -> bool:

        if request.method == 'GET':
            return request.user.role == 'SUPPORT' or request.user.role == 'SALER' or request.user.role == 'GESTION'
        if request.method == 'DELETE':
            return request.user.role == 'GESTION'
        return request.user.role == 'SALER' or request.user.role == 'GESTION'
    
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user == obj.sales_contact_id and request.user.role == 'SALER' or request.user.role == 'GESTION':
            return True

        