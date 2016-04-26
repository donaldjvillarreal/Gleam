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
# from spirit import urls as spirit_urls
# from qa import urls as qa_urls
# from caseconcept import urls as cc_urls
from core import urls as core_urls
from journal import urls as journal_urls
from therapist import urls as therapist_urls
from chat import urls as chat_urls
from tasks import urls as tasks_urls

urlpatterns = [
    url(r'', include(core_urls, namespace='core')),
    url(r'^users/', include(auth_urls, namespace='authenticate')),
    url(r'^survey/', include(diagnostic_urls, namespace='diagnostic')),
    # url(r'^spirit/', include(spirit_urls)),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^qa/', include(qa_urls, namespace='qa')),
    # url(r'^case/', include(cc_urls, namespace='case')),
    url(r'^journal/', include(journal_urls, namespace='journal')),
    url(r'^therapist/', include(therapist_urls, namespace='therapist')),
    url(r'^chat/', include(chat_urls, namespace='chat')),
    url(r'^tasks/', include(tasks_urls, namespace='tasks'))
]