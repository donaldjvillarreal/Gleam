# coding=utf-8
from django.conf.urls import url
from therapist import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^client/profile', views.client_profile, name='client_profile'),
]
