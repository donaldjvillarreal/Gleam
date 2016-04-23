# coding=utf-8
from django.conf.urls import url
from chat import views

urlpatterns = [
    url(r'^multichat/$', views.MultiChatView.as_view(), name='multichat_room'),
    url(r'^(?P<label>[\w-]+)/$', views.SingleChatView.as_view(), name='chat_room'),
]
