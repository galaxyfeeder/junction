from __future__ import unicode_literals

from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=5)
    longitude = models.DecimalField(max_digits=10, decimal_places=5)
    people_waiting = models.PositiveIntegerField(default=0)

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
    line = models.ForeignKey(Line)

    class Meta:
        unique_together = (('line', 'station'), ('line', 'order'))
        ordering = ('order',)

    def __unicode__(self):
        return self.line.number + " " + str(self.order) + ": " + self.station.name


class Bus(models.Model):
    code = models.CharField(max_length=10, unique=True)
    max_capacity = models.PositiveIntegerField()
    latitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    load = models.PositiveIntegerField(default=0, blank=True, null=True)
    line = models.ForeignKey(Line, null=True, blank=True)
    last_stop = models.ForeignKey(Stop, blank=True, null=True)
