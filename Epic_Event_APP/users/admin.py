from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'role', 'email', 'first_name', 'last_name', 'date_created', 'date_updated', 'id')
    fieldsets = ((None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'role',
                                    )}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        )
    
    def has_delete_permission(self, request, obj=None) -> bool:
        """prevent deleting the super user"""
        if obj is None:
            return True
        else:
            return not obj.is_superuser

            
admin.site.register(User, CustomUserAdmin)
