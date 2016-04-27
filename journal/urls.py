# coding=utf-8
from django.conf.urls import url
from journal import views

urlpatterns = [
    url(r'^$', views.list_view, name='listview'),
    url(r'^entry/$', views.entry, name='entry'),
    url(r'^words/$', views.word_list, name='words'),
    # url(r'^(?P<patient_id>[0-9]+)/therapist/$', views.TherapistTaskView.as_view(), name='create'),
]