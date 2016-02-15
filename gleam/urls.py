# coding=utf-8
"""gleam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from diagnostic import urls as diagnostic_urls
from authenticate import views as auth_views

urlpatterns = patterns('',
    url(r'^$', auth_views.index, name='index'),
    url(r'^register/$', auth_views.register, name='register'),
    url(r'^login/$', auth_views.user_login, name='login'),
    url(r'^logout/$', auth_views.user_logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^survey/', include(diagnostic_urls)),
)