from rest_framework import viewsets
from django.shortcuts import render
from django.views.generic import DetailView

from main.models import Line, Station, Bus
from main.serializers import BusSerializer, StationSerializer


class LineDetailView(DetailView):
    model = Line



class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class StationDisplayStaticView(DetailView):
    model = Station
    template_name = 'main/station_display_static.html'


class StationDisplayDynamicView(DetailView):
    model = Station
    template_name = 'main/station_display_dynamic.html'