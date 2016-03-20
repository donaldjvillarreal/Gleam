# coding=utf-8
"""
Email/SMS tasks
"""
from __future__ import absolute_import

from gleam.celery import app


@app.task
def send_email_notification(user_id=None):
    print 'HELLO!!!', user_id
