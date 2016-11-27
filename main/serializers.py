from rest_framework import serializers

from main.models import Bus, Station, Stop, Line


class SimpleStopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stop
        fields = ('id', 'order', 'line', 'people_waiting', 'people_leaving', 'travel_time')
        read_only_fields = ('id', 'order', 'line', 'travel_time')


class StationSerializer(serializers.HyperlinkedModelSerializer):
    stops = SimpleStopSerializer(many=True, read_only=True)

    class Meta:
        model = Station
        fields = ('id', 'name', 'code', 'latitude', 'longitude', 'stops')
        read_only_fields = ('id', 'name', 'code', 'latitude', 'longitude')


class SimpleStationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'name', 'code', 'latitude', 'longitude')
        read_only_fields = ('id', 'name', 'code', 'latitude', 'longitude')


class StopSerializer(serializers.HyperlinkedModelSerializer):
    station = SimpleStationSerializer(read_only=True)

    class Meta:
        model = Stop
        fields = ('id', 'order', 'station', 'line', 'people_waiting', 'people_leaving', 'travel_time')
        read_only_fields = ('id', 'order', 'station', 'line', 'travel_time')


class SimpleLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Line
        fields = ('number',)
        read_only_fields = ('number',)


class BusSerializer(serializers.HyperlinkedModelSerializer):
    line = SimpleLineSerializer(read_only=True)

    class Meta:
        model = Bus
        fields = ('id', 'code', 'max_capacity', 'latitude', 'longitude', 'load', 'line', 'last_stop_id')
        read_only_fields = ('id', 'code', 'max_capacity', 'latitude', 'longitude', 'line')


class SimpleBusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bus
        fields = ('code', 'max_capacity', 'latitude', 'longitude', 'load', 'last_stop_id')
        read_only_fields = ('code', 'max_capacity', 'latitude', 'longitude', 'load')


class LineSerializer(serializers.HyperlinkedModelSerializer):
    stops = StopSerializer(many=True)
    buses = SimpleBusSerializer(many=True)

    class Meta:
        model = Line
        fields = ('number', 'stops', 'buses', 'id')
        read_only_fields = ('number', 'stops', 'buses', 'id')
