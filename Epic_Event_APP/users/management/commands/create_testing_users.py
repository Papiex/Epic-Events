from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password

from users.models import User


class Command(BaseCommand):
    help = 'Create one user of each team (gestion ,support and saler)'

    
    def handle(self, *args, **options):

        if User.objects.filter(first_name='gestion_user') \
        and User.objects.filter(first_name='support_user') \
        and User.objects.filter(first_name='saler_user') \
        and User.objects.filter(first_name='admin_user'):
            self.stdout.write(self.style.ERROR(f'Users already created !'))
        else:
            gestion_group = Group.objects.get(name='Gestion Team')
            support_group = Group.objects.get(name='Support Team')
            saler_group = Group.objects.get(name='Saler Team')

            gestion_user = User.objects.create(
                role = 'GESTION',
                username = 'gestion_user',
                first_name = 'gestion_user',
                last_name = 'gestion_user',
                email = 'gestion_user@mail.fr'
            )
            gestion_user.groups.add(gestion_group)
            saler_user = User.objects.create(
                role = 'SALER',
                username = 'saler_user',
                first_name = 'saler_user',
                last_name = 'saler_user',
                email = 'saler_user@mail.fr'
            )
            saler_user.groups.add(saler_group)
            support_user = User.objects.create(
                role = 'SUPPORT',
                username = 'support_user',
                first_name = 'support_user',
                last_name = 'support_user',
                email = 'support_user@mail.fr'
            )
            support_user.groups.add(support_group)

            admin_user = User.objects.create(
                role = 'ADMIN',
                username = 'admin_user',
                first_name = 'admin_user',
                last_name = 'admin_user',
                email = 'admin_user@mail.fr',
                is_superuser = True,
                is_staff = True
            )
            gestion_user.set_password('motdepasse78')
            gestion_user.save()
            support_user.set_password('motdepasse78')
            support_user.save()
            saler_user.set_password('motdepasse78')
            saler_user.save()
            admin_user.set_password('motdepasse78')
            admin_user.save()

            if User.objects.filter(first_name='gestion_user') \
            and User.objects.filter(first_name='support_user') \
            and User.objects.filter(first_name='saler_user') \
            and User.objects.filter(first_name='admin_user'):
                self.stdout.write(self.style.SUCCESS(f'Successfully created Gestion, Saler and Support User, check the README for the users identifers'))
            else:
                self.stdout.write(self.style.ERROR(f'Somenthing went wrong with the command, please try again'))
