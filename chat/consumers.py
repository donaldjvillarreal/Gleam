# coding=utf-8
from django.contrib.auth.models import User
import json
import dateutil.parser

from channels import Group
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
from chat import models


# Connected to chat-messages
@channel_session_user
def msg_consumer(message):
    # Save to model
    room = message.content['path'].strip("/")
    json_message = json.loads(message.content['text'])
    models.ChatMessage.objects.create(
        room=room,
        message=json_message['message'],
        timestamp=dateutil.parser.parse(json_message['timestamp']),
        user=User.objects.get(id=message.user.id)
    )
    # Broadcast to listening sockets
    Group("%i" % message.user.id).send({
        "text": json_message['message'],
    })


# Connected to websocket.connect
@channel_session_user_from_http
def ws_connect(message):
    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip("/")
    # Save room in session and add us to the group
    message.channel_session['room'] = room
    Group("%i" % message.user.id).add(message.reply_channel)


# Connected to websocket.receive
@channel_session_user
def ws_message(message):
    Group("%i" % message.user.id).send({
        "text": message['text'],
    })


# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    Group("%i" % message.user.id).discard(message.reply_channel)
