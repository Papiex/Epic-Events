from django_filters import rest_framework as filters

from events.models import Event


class EventFilterSet(filters.FilterSet):
    email = filters.CharFilter(field_name='customer_id__email')
    last_name = filters.CharFilter(field_name='customer_id__last_name')

    class Meta:
        model = Event
        fields = [
            'event_date',
            ]