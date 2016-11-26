from rest_framework import viewsets
from django.shortcuts import render
from django.views.generic import DetailView

from main.models import Line, Station, Bus
from main.serializers import BusSerializer, StationSerializer


class LineDetailView(DetailView):
    model = Line



class StationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class BusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
