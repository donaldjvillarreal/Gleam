# coding=utf-8
from django.conf.urls import url
from journal import views

urlpatterns = [
    url(r'^$', views.entry, name='entry'),
    url(r'^history/$', views.list_view, name='listview'),
    url(r'^entry/$', views.entry, name='entry'),
    url(r'^words/$', views.word_list, name='words'),
]