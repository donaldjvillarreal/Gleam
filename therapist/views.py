# coding=utf-8
from django.shortcuts import render


def index(request):
    return render(request, 'therapist/feed.html', {'people': range(10)})
