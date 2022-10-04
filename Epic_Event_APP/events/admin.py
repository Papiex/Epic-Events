from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'customer_id',
        'date_created',
        'date_updated',
        'support_contact_id',
        'event_statut_id',
        'attendees',
        'event_date',
        'notes',
        'contract_id',
        )


admin.site.register(Event, EventAdmin)
