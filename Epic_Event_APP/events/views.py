from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .models import Event
from .serializers import EventSerializer
from .permissions import EventPermission
from .filters import EventFilterSet


class EventViewSet(viewsets.ModelViewSet):
    filterset_class = EventFilterSet
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [EventPermission, IsAuthenticated]
