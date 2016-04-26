# coding=utf-8
from django.conf.urls import url
from tasks import views

urlpatterns = [
    url(r'^(?P<patient_id>[0-9]+)/$', views.CreateHomework.as_view(), name='create'),
]
