from django.shortcuts import render
from .models import Choice
import pandas as pd
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


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

    return HttpResponseRedirect(reverse('plot_app:choice'))
