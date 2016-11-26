from rest_framework import serializers

from main.models import Bus, Station, Stop, Line


class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ('name', 'code', 'latitude', 'longitude', 'people_waiting')
        read_only_fields = ('name', 'code', 'latitude', 'longitude')


class StopSerializer(serializers.HyperlinkedModelSerializer):
    station = StationSerializer(read_only=True)

    class Meta:
        model = Stop
        fields = ('order', 'station')
        read_only_fields = ('order', 'station')


class LineSerializer(serializers.HyperlinkedModelSerializer):
    stops = StopSerializer(many=True)

    class Meta:
        model = Line
        fields = ('number', 'stops')
        read_only_fields = ('number', 'stops')


class BusSerializer(serializers.HyperlinkedModelSerializer):
    line = LineSerializer(read_only=True)

    class Meta:
        model = Bus
        fields = ('code', 'max_capacity', 'latitude', 'longitude', 'load', 'line', 'last_stop')
        read_only_fields = ('code', 'max_capacity', 'latitude', 'longitude', 'line')
