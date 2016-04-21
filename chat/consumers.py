# coding=utf-8
from django.contrib.auth.models import User
import json
from datetime import datetime

from channels import Group
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
from chat import models


# https://github.com/andrewgodwin/channels-examples/tree/master/multichat

# Connected to websocket.connect
@channel_session_user_from_http
def ws_connect(message):
    print message.content
    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip("/")
    # Save room in session and add us to the group
    message.channel_session['room'] = room
    Group("room-%i" % message.user.id).add(message.reply_channel)


# Connected to websocket.receive
@channel_session_user
def ws_receive(message):
    Group("%i" % message.user.id).send({
        "text": message['text'],
    })


# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    Group("%i" % message.user.id).discard(message.reply_channel)


# Connected to chat-messages
@channel_session_user
def msg_consumer(message):
    # Save to model
    room = message.content['path'].strip("/")
    json_message = json.loads(message.content['text'])
    models.Message.objects.create(
        room=room,
        message=json_message['message'],
        timestamp=datetime.fromtimestamp(int(json_message['timestamp']) / 1000.0),
        user=User.objects.get(id=message.user.id)
    )
    # Broadcast to listening sockets
    Group("%i" % message.user.id).send({
        "text": json_message['message'],
    })


# Channel_session_user loads the user out from the channel session and presents
# it as message.user. There's also a http_session_user if you want to do this on
# a low-level HTTP handler, or just channel_session if all you want is the
# message.channel_session object without the auth fetching overhead.
@channel_session_user
def chat_join(message):
    # Find the room they requested (by ID) and add ourselves to the send group
    # Note that, because of channel_session_user, we have a message.user
    # object that works just like request.user would. Security!
    room = (message["room"], message.user)
    # OK, add them in. The websocket_group is what we'll send messages
    # to so that everyone in the chat room gets them.
    room.websocket_group.add(message.reply_channel)
    message.channel_session['rooms'] = list(set(message.channel_session['rooms']).union([room.id]))
    # Send a message back that will prompt them to open the room
    # Done server-side so that we could, for example, make people
    # join rooms automatically.
    message.reply_channel.send({
        "text": json.dumps({
            "join": str(room.id),
            "title": room.title,
        }),
    })


@channel_session_user
def chat_leave(message):
    # Reverse of join - remove them from everything.
    room = (message["room"], message.user)
    room.websocket_group.discard(message.reply_channel)
    message.channel_session['rooms'] = list(set(message.channel_session['rooms']).difference([room.id]))
    # Send a message back that will prompt them to close the room
    message.reply_channel.send({
        "text": json.dumps({
            "leave": str(room.id),
        }),
    })


@channel_session_user
def chat_send(message):
    # Find the room they're sending to, check perms
    room = (message["room"], message.user)
    # Send the message along
    room.send_message(message["message"], message.user)
