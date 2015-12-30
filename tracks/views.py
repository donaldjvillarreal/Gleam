# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Main functions of tracks views
    :param request:
    :return:
    """
    return HttpResponse('OK')
