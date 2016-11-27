from django.http import JsonResponse
from rest_framework import viewsets
from django.views.generic import DetailView

from main.models import Line, Station, Bus, Stop
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


class StationDisplayStaticView(DetailView):
    model = Station
    template_name = 'main/station_display_static.html'


class StationDisplayDynamicView(DetailView):
    model = Station
    template_name = 'main/station_display_dynamic.html'


def add_view(request, stop_id):

    stop = Stop.objects.get(pk=stop_id)

    stop.people_waiting += 1
    stop.save()

    return JsonResponse({'success': True})