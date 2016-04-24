# coding=utf-8
"""
https://github.com/jacobian/channels-example/blob/master/chat/consumers.py
"""
from django.contrib.auth.models import User
import json
from channels import Channel
from channels.auth import channel_session_user_from_http, channel_session_user
from models import Room

from authenticate.models import UserProfile


@channel_session_user_from_http
def ws_connect(message):
    # Initialise their session
    message.channel_session['rooms'] = []
    try:
        user_profile = UserProfile.objects.get(user__username=message.user.username)
        if user_profile.is_therapist:
            for room in Room.objects.filter(therapist__username=message.user.username):
                message['room'] = room.id
                chat_join(message)
        else:
            message['room'] = Room.objects.get(patient__username=message.user.username).id
            chat_join(message)
    except UserProfile.DoesNotExist:
        pass


def ws_receive(message):
    # All WebSocket frames have either a text or binary payload; we decode the
    # text part here assuming it's JSON.
    # You could easily build up a basic framework that did this encoding/decoding
    # for you as well as handling common errors.
    payload = json.loads(message['text'])
    payload['reply_channel'] = message.content['reply_channel']
    Channel("chat.receive").send(payload)


@channel_session_user
def ws_disconnect(message):
    for room_id in message.channel_session.get("rooms", set()):
        try:
            room = Room.objects.get(pk=room_id)
            # Removes us from the room's send group. If this doesn't get run,
            # we'll get removed once our first reply message expires.
            room.websocket_group.discard(message.reply_channel)
        except Room.DoesNotExist:
            pass


@channel_session_user
def chat_join(message):
    room = Room.objects.get(id=message["room"])
    # OK, add them in. The websocket_group is what we'll send messages
    # to so that everyone in the chat room gets them.
    room.websocket_group.add(message.reply_channel)
    message.channel_session['rooms'] = list(set(message.channel_session['rooms']).union([room.id]))
    # Send a message back that will prompt them to open the room
    # Done server-side so that we could, for example, make people
    # join rooms automatically.
    user_id = message.user.id
    if user_id == room.therapist_id:
        title = room.therapist.username
    elif user_id == room.patient_id:
        title = room.patient.username
    else:
        title = message.user
    old_messages = [old_message.as_dict() for old_message in room.messages.all()]
    message.reply_channel.send({
        "text": json.dumps({
            "join": str(room.id),
            "title": title,
            "therapist": room.therapist_as_dict(),
            "patient": room.patient_as_dict(),
            'old_messages': old_messages
        }),
    })


@channel_session_user
def chat_send(message):
    # Find the room they're sending to, check perms
    room = Room.objects.get(id=message["room"])
    # Send the message along and store it
    if 'urgency' in message:
        stored_message = room.messages.create(handle=User.objects.get(id=message.user.id),
                                              message=message['message'],
                                              urgency=message['urgency'])
        room.send_message(message["message"], message.user, stored_message.formatted_timestamp, message['urgency'])
    else:
        stored_message = room.messages.create(handle=User.objects.get(id=message.user.id),
                                              message=message['message'])
        room.send_message(message["message"], message.user, stored_message.formatted_timestamp)


@channel_session_user
def chat_leave(message):
    # Reverse of join - remove them from everything.
    room = Room.objects.get(id=message["room"])
    room.websocket_group.discard(message.reply_channel)
    message.channel_session['rooms'] = list(set(message.channel_session['rooms']).difference([room.id]))
    # Send a message back that will prompt them to close the room
    message.reply_channel.send({
        "text": json.dumps({
            "leave": str(room.id),
        }),
    })
