# coding=utf-8
"""
URLs for core app
"""

from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]