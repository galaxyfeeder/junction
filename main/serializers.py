from rest_framework import serializers

from main.models import Bus, Station


class StationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Station
        fields = ('name', 'code', 'latitude', 'longitude', 'people_waiting')
        read_only_fields = ('name', 'latitude', 'longitude')


class BusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bus
        fields = ('code', 'max_capacity', 'latitude', 'longitude', 'load', 'line', 'last_stop')
        read_only_fields = ('code', 'max_capacity', 'latitude', 'longitude', 'line')
