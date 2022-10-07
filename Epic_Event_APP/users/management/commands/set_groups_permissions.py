from itertools import chain
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'Add model permission for the supports and the salers groups'


    def handle(self, *args, **options):

        salers_group = Group.objects.get(name='Saler Team')
        supports_group = Group.objects.get(name='Support Team')
        gestions_group = Group.objects.get(name='Gestion Team')
        saler_permissions = self.get_saler_permissions()
        support_permissions = self.get_support_permissions()
        gestion_permissions = self.get_gestion_permissions()

        for permission in support_permissions:
            try:
                supports_group.permissions.add(permission)
            except permission.DoesNotExist:
                raise CommandError(f'the permission {permission} does not exist')
        for permission in saler_permissions:
            try:
                salers_group.permissions.add(permission)
            except permission.DoesNotExist:
                raise CommandError(f'the permission {permission} does not exist')    
        for permission in gestion_permissions:
            try:
                gestions_group.permissions.add(permission)
            except permission.DoesNotExist:
                raise CommandError(f'the permission {permission} does not exist')    
        
        self.stdout.write(self.style.SUCCESS(f'Permissions for the {supports_group.name} have been added successfully'))
        self.stdout.write(self.style.SUCCESS(f'Permissions for the {salers_group.name} have been added successfully'))
        self.stdout.write(self.style.SUCCESS(f'Permissions for the {gestions_group.name} have been added successfully'))


    def get_saler_permissions(self):
        """Get and return the correct permission for salers team"""
        customer_content_type = ContentType.objects.get(app_label='customers', model='customer')
        customer_permissions = Permission.objects.filter(content_type=customer_content_type).exclude(name='Can delete customer')
        contract_content_type = ContentType.objects.get(app_label='contracts', model='contract')
        contract_permissions = Permission.objects.filter(content_type=contract_content_type).exclude(name='Can delete contract')
        event_content_type = ContentType.objects.get(app_label='events', model='event')
        event_permission = Permission.objects.filter(content_type=event_content_type).exclude(name='Can delete event')

        permissions = chain(customer_permissions, contract_permissions, event_permission)

        return permissions
    

    def get_support_permissions(self):
        """Get and return the correct permission for supports team"""
        customer_content_type = ContentType.objects.get(app_label='customers', model='customer')
        customer_permissions = Permission.objects.filter(content_type=customer_content_type).filter(name='Can view customer')
        contract_content_type = ContentType.objects.get(app_label='contracts', model='contract')
        contract_permissions = Permission.objects.filter(content_type=contract_content_type).filter(name='Can view contract')
        event_content_type = ContentType.objects.get(app_label='events', model='event')
        event_permission = Permission.objects.filter(content_type=event_content_type).exclude(name='Can delete event').exclude(name='Can add event')

        permissions = chain(customer_permissions, contract_permissions, event_permission)

        return permissions


    def get_gestion_permissions(self):
        """Get and return the correct permission for supports team"""
        user_content_type = ContentType.objects.get(app_label='users', model='user')
        user_permissions = Permission.objects.filter(content_type=user_content_type).exclude(name='To create Customers')
        customer_content_type = ContentType.objects.get(app_label='customers', model='customer')
        customer_permissions = Permission.objects.filter(content_type=customer_content_type).exclude(name='Can delete customer')
        contract_content_type = ContentType.objects.get(app_label='contracts', model='contract')
        contract_permissions = Permission.objects.filter(content_type=contract_content_type).exclude(name='Can delete contract')
        event_content_type = ContentType.objects.get(app_label='events', model='event')
        event_permission = Permission.objects.filter(content_type=event_content_type).exclude(name='Can delete event')

        permissions = chain(user_permissions, customer_permissions, contract_permissions, event_permission)

        return permissions
