from __future__ import unicode_literals

from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=10, decimal_places=5)
    longitude = models.DecimalField(max_digits=10, decimal_places=5)
    people_waiting = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = (('latitude', 'longitude'),)


class Line(models.Model):
    number = models.CharField(max_length=10, unique=True)


class Stop(models.Model):
    order = models.PositiveIntegerField()
    station = models.ForeignKey(Station)
    line = models.ForeignKey(Line)

    class Meta:
        unique_together = (('line', 'station'), ('line', 'order'))


class Bus(models.Model):
    code = models.CharField(max_length=10)
    max_capacity = models.PositiveIntegerField()
    latitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    load = models.PositiveIntegerField(default=0, blank=True, null=True)
    line = models.ForeignKey(Line, null=True, blank=True)
    last_stop = models.ForeignKey(Stop, blank=True, null=True)
