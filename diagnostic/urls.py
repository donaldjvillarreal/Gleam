# coding=utf-8
from django.conf.urls import url
from diagnostic import views


urlpatterns = [
    url(r'^hamd/$', views.hamd_survey, name='hamd_survey'),
    url(r'^bdi/$', views.bdi_survey, name='bdi_survey'),
]