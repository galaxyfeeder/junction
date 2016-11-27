from __future__ import unicode_literals

from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)

    class Meta:
        unique_together = (('latitude', 'longitude'),)

    def __unicode__(self):
        return self.code + ": " + self.name + "(" + str(self.latitude) + ", " + str(self.longitude) + ")"


class Line(models.Model):
    number = models.CharField(max_length=10, unique=True)

    def __unicode__(self):
        return "Line " + self.number


class Stop(models.Model):
    order = models.PositiveIntegerField()
    station = models.ForeignKey(Station)
    line = models.ForeignKey(Line, related_name='stops')
    people_waiting = models.PositiveIntegerField(default=0)
    people_leaving = models.PositiveIntegerField(default=0)
    travel_time = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = (('line', 'station'), ('line', 'order'))
        ordering = ('order',)

    def __unicode__(self):
        return self.line.number + " " + str(self.order) + ": " + self.station.name

    def _will_stop(self):
        return not (self.people_waiting == 0 and self.people_leaving == 0)

    will_stop=property(_will_stop)

    def stop_time(self):
        return 10 + max(self.people_waiting, self.people_leaving) * 3

    def stopped(self):
        self.people_waiting = 0
        self.people_leaving = 0
        self.save()

    def destination_travel_time(self, destination_stop):
        stops = Stop.objects.filter(line=self.line, order__gt=self, order__lte=destination_stop)
        traveltime = 0
        for stop in stops:
            traveltime += stop.travel_time + stop.stop_time()
        return traveltime


class Bus(models.Model):
    code = models.CharField(max_length=10, unique=True)
    max_capacity = models.PositiveIntegerField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    load = models.PositiveIntegerField(default=0, blank=True, null=True)
    line = models.ForeignKey(Line, null=True, blank=True, related_name='buses')
    last_stop = models.ForeignKey(Stop, blank=True, null=True)
