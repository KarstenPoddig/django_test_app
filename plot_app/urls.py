from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ChoiceView.as_view(), name='choice'),
    url(r'^(?P<choice_id>[0-9]+)/vote/$', views.klick, name='klick'),


    # Bar chart
    # url(r'^klick_bar_chart/$', views.klick_bar_chart,
    #     name='klick_bar_chart'),
    url(r'^klick_bar_chart/json/$', views.klick_bar_chart_json,
        name='klick_bar_chart_json'),
]
