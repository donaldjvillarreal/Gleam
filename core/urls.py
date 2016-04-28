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
    url(r'^therapist/$', views.therapist_home, name='therapist_home'),
    url(r'^therapist/patient/$', views.patient_list, name='patient_list'),
    url(r'^therapist/patient/(?P<patient_id>[0-9]+)/$', views.patient_list, name='patient_profile'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]