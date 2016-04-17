# coding=utf-8
from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class IndexView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'chat/index.html', {'room': request.user.id})
