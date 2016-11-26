from rest_framework import viewsets
from django.views.generic import DetailView

from main.models import Line, Station, Bus
from main.serializers import BusSerializer, StationSerializer, LineSerializer


class LineDetailView(DetailView):
    model = Line


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class LineViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LineSerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
