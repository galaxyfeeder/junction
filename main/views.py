from django.shortcuts import render
from django.views.generic import DetailView

from main.models import Line


class LineDetailView(DetailView):
    model = Line

