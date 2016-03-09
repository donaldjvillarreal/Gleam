from django.conf.urls import url, include, patterns
from django.contrib import admin
from diagnostic import urls as diagnostic_urls
from caseconcept import views

urlpatterns = [
    url(r'^calendar/$', views.cal, name='calendar'),
]