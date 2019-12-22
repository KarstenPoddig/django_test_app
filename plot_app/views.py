from django.shortcuts import render
from .models import Choice
import pandas as pd
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


# Create your views here.


class ChoiceView(generic.ListView):
    template_name = 'choice.html'
    context_object_name = 'choice_list'

    def get_queryset(self):
        return Choice.objects.all()


def klick(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)

    choice.number += 1
    choice.save()

    return HttpResponseRedirect(reverse('choice'))


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
