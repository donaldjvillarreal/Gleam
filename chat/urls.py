# coding=utf-8
from django.conf.urls import url
from chat import views

urlpatterns = [
    url(r'^multichat/$', views.ChatView.as_view(), name='multichat_room'),
]
