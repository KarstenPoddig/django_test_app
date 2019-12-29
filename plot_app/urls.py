from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^choice_new/$', views.ChoiceNewView.as_view(),
        name='choice_new'),

    # JSON-Response
    url(r'^choice/json/$', views.klickJSON, name='choice_json'),


    # Bar chart
    # url(r'^klick_bar_chart/$', views.klick_bar_chart,
    #     name='klick_bar_chart'),
    url(r'^klick_bar_chart/json/$', views.klick_bar_chart_json,
        name='klick_bar_chart_json'),

    # form test
    # url(r'^form_test/', views.form_test, name='form_test'),
    url(r'^$', views.choice_view, name='choice'),
]
