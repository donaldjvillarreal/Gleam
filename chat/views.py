# coding=utf-8
from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from models import Room


class ChatView(View):
    @method_decorator(login_required)
    def get(self, request, label):
        room = Room.objects.get(label=label)

        # We want to show the last 50 messages, ordered most-recent-last
        messages = reversed(room.messages.order_by('-timestamp')[:50])

        return render(request, "chat/room.html", {
            'room': room,
            'messages': messages,
        })
