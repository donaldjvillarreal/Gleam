# coding=utf-8
from django.shortcuts import render


def index(request):
    return render(request, 'therapist/feed.html', {'people': range(10)})


def client_profile(request):
    return render(request, 'therapist/client-profile.html', {})
