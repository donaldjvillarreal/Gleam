# coding=utf-8
"""
https://github.com/jacobian/channels-example/blob/master/chat/consumers.py
"""
from django.contrib.auth.models import User
import logging
import json
from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user_from_http, channel_session_user
from models import Room

log = logging.getLogger(__name__)


@channel_session_user_from_http
def ws_connect(message):
    # Extract the room from the message. This expects message.path to be of the
    # form /chat/{label}/, and finds a Room if the message path is applicable
    prefix, label = None, None
    try:
        prefix, label = message['path'].decode('ascii').strip('/').split('/')
        if prefix != 'chat':
            log.debug('invalid ws path=%s', message['path'])
            return
        room = Room.objects.get(label=label)
    except ValueError:
        log.debug('invalid ws path=%s', message['path'])
        return
    except Room.DoesNotExist:
        log.debug('ws room does not exist label=%s', label)
        return

    log.debug('chat connect room=%s client=%s:%s',
              room.label, message['client'][0], message['client'][1])

    Group('chat-' + label, channel_layer=message.channel_layer).add(message.reply_channel)

    message.channel_session['room'] = room.label


@channel_session_user
def ws_receive(message):
    # Look up the room from the channel session, bailing if it doesn't exist
    label, room = None, None
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
    except KeyError:
        log.debug('no room in channel_session')
        return
    except Room.DoesNotExist:
        log.debug('received message, buy room does not exist label=%s', label)
        return

    # Parse out a chat message from the content text, bailing if it doesn't
    # conform to the expected message format.
    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text=%s", message['text'])
        return

    if data:
        log.debug('chat message room=%s handle=%s message=%s',
                  room.label, message.user.username, data['message'])
        m = room.messages.create(handle=User.objects.get(id=message.user.id),
                                 message=data['message'])

        # See above for the note about Group
        Group('chat-' + label, channel_layer=message.channel_layer).send({'text': json.dumps(m.as_dict())})


@channel_session
def ws_disconnect(message):
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
        Group('chat-' + label, channel_layer=message.channel_layer).discard(message.reply_channel)
    except (KeyError, Room.DoesNotExist):
        pass
