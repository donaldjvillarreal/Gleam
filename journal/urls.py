# coding=utf-8
from django.conf.urls import url
from journal import views

urlpatterns = [
    #url(r'^$', views.case_index, name='index'),
    url(r'^entry/$', views.journalEntry, name='entry'),
    url(r'^words/$', views.wordListView, name='words'),
]