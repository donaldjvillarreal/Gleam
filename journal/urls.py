# coding=utf-8
from django.conf.urls import url
from journal import views

urlpatterns = [
    url(r'^$', views.entry, name='entry'),
    url(r'^history/$', views.list_view, name='history'),
    url(r'^entry/$', views.entry, name='entry'),
    url(r'^entry/(?P<entry_id>[0-9]+)/$', views.view_entry, name='view_entry'),
    url(r'^words/$', views.word_list, name='words'),
]
