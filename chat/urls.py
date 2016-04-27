# coding=utf-8
from django.conf.urls import url
from chat import views

urlpatterns = [
    url(r'^$', views.ChatView.as_view(), name='chat_room'),
]
