from rest_framework import viewsets

from main.models import Station, Bus
from main.serializers import StationSerializer, BusSerializer


class StationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class BusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
