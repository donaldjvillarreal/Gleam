# coding=utf-8
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from models import Room


class SingleChatView(View):
    @method_decorator(login_required)
    def get(self, request, label):
        room = Room.objects.get(label=label)

        # We want to show the last 50 messages, ordered most-recent-last
        messages = reversed(room.messages.order_by('-timestamp')[:50])

        return render(request, "chat/room.html", {
            'room': room,
            'messages': messages,
        })


class MultiChatView(View):
    @method_decorator(login_required)
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        messages = []
        if user.userprofile.is_therapist:
            # user is a therapist
            rooms = Room.objects.filter(therapist=user)
            for room in rooms:
                messages.append((room, reversed(room.messages.order_by('-timestamp')[:30])))
            return render(request, 'chat/therapist-multichat.html', {'messages': messages})

        else:
            room = Room.objects.get(patient=user)
            messages.append((room, reversed(room.messages.order_by('-timestamp')[:30])))
            return render(request, 'chat/patient-chat.html', {'messages': messages})
