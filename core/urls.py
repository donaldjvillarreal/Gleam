# coding=utf-8
"""
URLs for core app
"""

from django.conf.urls import url
from core import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^progress/check/$', views.progress_delay, name='progress_check'),
    url(r'^patient/$', views.PatientHomeView.as_view(), name='patient_home'),
]
