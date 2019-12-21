from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'plot_app'
urlpatterns = [
    url(r'^$', views.ChoiceView.as_view(), name='choice'),
    url(r'^(?P<choice_id>[0-9]+)/vote/$', views.klick, name='klick'),
]
