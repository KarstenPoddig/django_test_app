from django.shortcuts import render
from .models import Choice
import pandas as pd
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
import pandas as pd
from django.core import serializers
from django.forms import formset_factory
from .forms import ChoiceModel
from django.views import View

# Create your views here.


class ChoiceNewView(generic.ListView):
    template_name = 'choice_new.html'
    context_object_name = 'choice_list'

    def get_queryset(self):
        return Choice.objects.all()


def choice_view(request):

    choices = Choice.objects.all()

    if request.method == 'POST':
        form = ChoiceModel(request.POST)
        choice = choices.get(id=request.POST['choice_id'])
        choice.number += 1
        choice.save()

    else:
        form = ChoiceModel(initial={'number': 0})

    context = {
        'form': form,
        'choices': choices,
    }

    return render(request, context=context,
                  template_name='choice.html')



def klickJSON(request):
    # data = serializers.serialize("json", Choice.objects.all())
    df = pd.DataFrame.from_records(Choice.objects.all().values())
    return JsonResponse(df.to_dict(),
                        safe=False)


def klick(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)

    choice.number += 1
    choice.save()

    return HttpResponseRedirect(reverse('choice'))


class KlickJSONView(BaseLineChartView):

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        df = pd.DataFrame.from_records(Choice.objects.all().values())
        return df['name'].tolist()

    def get_providers(self):
        """Return names of datasets."""
        df = pd.DataFrame.from_records(Choice.objects.all().values())
        return ["Gruppe 1"]

    def get_data(self):
        """Return 3 datasets to plot."""
        df = pd.DataFrame.from_records(Choice.objects.all().values())
        return [df['number'].tolist()]


klick_bar_chart = TemplateView.as_view(template_name='choice.html')
klick_bar_chart_json = KlickJSONView.as_view()
