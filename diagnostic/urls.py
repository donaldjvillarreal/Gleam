# coding=utf-8
from django.conf.urls import url
from diagnostic import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bdi/$', views.bdi_survey_pagination, name='bdi_survey'),
    url(r'^bdi/score/$', views.bdi_score, name='bdi_score'),
]
