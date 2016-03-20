# coding=utf-8
"""
Email/SMS tasks
"""
from __future__ import absolute_import
import urllib, urllib2

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf.global_settings import EMAIL_HOST_USER

from gleam.celery import app
from authenticate.models import UserProfile


@app.task
def send_notifications(user_id=None):
    print 'HELLO!!!'
    subject = 'Gleam: You have an upcoming goal/activity scheduled!'
    user_profile = UserProfile.objects.get(user=User.objects.get(id=user_id))
    if user_profile.email:
        send_mail(subject=subject,
                  message=render_to_string('notifications/reminder_email.txt', {'user_profile': user_profile}),
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user_profile.email],
                  html_message=render_to_string('notifications/reminder_email.html', {'user_profile': user_profile}))
    if user_profile.phone:
        send_text(user_profile.phone,
                  render_to_string('notifications/reminder_email.txt', {'user_profile': user_profile}))


def send_text(number, message):
    data = urllib.urlencode({'number': number, 'message': message})
    r = urllib2.urlopen('http://textbelt.com/text', data)
    return r.getcode(), r.read()
