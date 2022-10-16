from django.contrib import admin

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'mobile',
        'company_name',
        'date_created',
        'date_updated',
        'sales_contact_id',
        'customer_type',
        'id',
    )


admin.site.register(Customer, CustomerAdmin)