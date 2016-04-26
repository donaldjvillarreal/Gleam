# coding=utf-8
from django.conf.urls import url
from tasks import views


urlpatterns = [
    url(r'^createHW/$', views.CreateHomework, name='CreateHomework'),
]
