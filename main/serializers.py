from rest_framework import serializers

from main.models import Bus, Station


class StationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Station
        fields = ('name', 'latitude', 'longitude', 'people_waiting')
        read_only_fields = ('name', 'latitude', 'longitude')


class BusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bus
        fields = ('', '', '', '', '')
