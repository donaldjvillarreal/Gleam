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
from django.conf.urls import url, include
from django.contrib import admin
from diagnostic import urls as diagnostic_urls
from authenticate import urls as auth_urls
from spirit import urls as spirit_urls
from qa import urls as qa_urls
from caseconcept import urls as cc_urls

urlpatterns = [
    url(r'^users/', include(auth_urls, namespace='authenticate')),
    url(r'^survey/', include(diagnostic_urls, namespace='diagnostic')),
    url(r'^spirit/', include(spirit_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^qa/', include(qa_urls, namespace='qa')),
    url(r'^caseconcept/', include(cc_urls)),
]