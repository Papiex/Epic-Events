from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .models import Event
from .serializers import EventSerializer
from .permissions import EventPermission


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [EventPermission, IsAuthenticated]
    filterset_fields = [
        "customer_id__last_name",
        "customer_id__email",
        "event_date",
    ]
