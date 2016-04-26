# coding=utf-8
from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from authenticate.models import Therapist, UserProfile
from tasks.models import MainTask
from tasks import forms


class CreateHomework(View):
    @method_decorator(login_required)
    def get(self, request, patient_id):
        return render(request, 'tasks/create-task.html',
                      {'tasks': MainTask.objects.filter(patient__user_id=patient_id)})

    @method_decorator(login_required)
    def post(self, request, patient_id):
        task_form = forms.MainTaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.therapist = Therapist.objects.get(user_profile__user=request.user.id)
            task.patient = UserProfile.objects.get(user_id=patient_id)
            task.created = datetime.now()
            task.save()
        else:
            print task_form.errors
        return HttpResponseRedirect('')
