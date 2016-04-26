# coding=utf-8
from django.shortcuts import render
from django.views.generic import View
from tasks import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime
from authenticate.models import Client, Therapist, UserProfile
from tasks.models import MainTask


class CreateHomework(View):
    @method_decorator(login_required)
    def get(self, request, patient_id):
        return render(request, 'tasks/create-task.html', {})

    @method_decorator(login_required)
    def post(self, request, patient_id):
        print request.POST
        task_form = forms.MainTaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.therapist = Therapist.objects.get(user_profile__user=request.user.id)
            task.patient = UserProfile.objects.get(user_id=patient_id)
            task.created = datetime.now()
            task.save()
        else:
            print task_form.errors
        return render(request, 'tasks/create-task.html', {})
