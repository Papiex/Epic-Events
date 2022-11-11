from django.db import models
from django.contrib.auth.models import AbstractUser, Group

from .enums import StaffRole


class User(AbstractUser):
    """Custom User Model"""

    role = models.CharField(
        max_length=16, choices=[(role.name, role.value) for role in StaffRole]
    )
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    email = models.EmailField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """add the user to a specific group according to their role"""
        if not self.id:
            super(User, self).save(*args, **kwargs)
        else:
            if self.role == "GESTION":
                self.groups.add(Group.objects.get(name="Gestion Team"))
            elif self.role == "SUPPORT":
                self.groups.add(Group.objects.get(name="Support Team"))
            elif self.role == "SALER":
                self.groups.add(Group.objects.get(name="Saler Team"))
                print(self.groups)
            super(User, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.username) + " " + str(self.id)
