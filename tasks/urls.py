# coding=utf-8
from django.conf.urls import url
from tasks import views

urlpatterns = [
    url(r'^(?P<patient_id>[0-9]+)/therapist/$', views.TherapistTaskView.as_view(), name='create'),
    url(r'^complete/$', views.PatientTaskView.as_view(), name='complete'),
]
