from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ChoiceView.as_view(), name='choice'),
    url(r'^(?P<choice_id>[0-9]+)/vote/$', views.klick, name='klick'),

    # Line chart
    url(r'^line_chart/$', views.line_chart,
        name='line_chart'),
    url(r'^line_chart/json/$', views.line_chart_json,
        name='line_chart_json'),
]
