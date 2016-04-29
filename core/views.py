# coding=utf-8
import json
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.utils.timezone import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from core import forms
from tasks.models import MainTask
from journal.models import Entry, Note
from authenticate.models import Client

MAX_ROWS = 5


def index(request):
    return render(request, 'index.html', {})


@login_required()
def progress_delay(request):
    if request.method == 'POST':
        progress_issue = forms.ProgressIssueForm(request.POST)
        if progress_issue.is_valid():
            progress_issue = progress_issue.save(commit=False)
            progress_issue.user = User.objects.get(id=request.user.id)
            progress_issue.save()
            if request.GET.get('courses', None) is not None:
                return HttpResponseRedirect(reverse('case:start_course'))
            else:
                print request.GET
                return HttpResponseRedirect('/')
        else:
            return render(request, 'core/progress-delay.html', {'errors': progress_issue.errors})
    else:
        return render(request, 'core/progress-delay.html', {})


@login_required()
def therapist_home(request):
    # TODO order clients by last appointment/different metric
    return render(request, 'core/therapist-dashboard/content-tp-dash.html', {
        'notes': Note.objects.filter(therapist__user_profile__user_id=request.user.id)[:MAX_ROWS],
        'clients': Client.objects.filter(therapist__user_profile__user_id=request.user.id)[:MAX_ROWS]
    })


def landing(request):
    return render(request, 'core/landing/landing.html', {})


class PatientHomeView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'core/dashboard/patient-home.html',
                      {'tasks': MainTask.objects.filter(patient__user_id=request.user.id, completed=False).order_by(
                          'created')[:MAX_ROWS],
                       'journals': Entry.objects.filter(user_id=request.user.id).order_by('-created')[:MAX_ROWS]
                       })

    @method_decorator(login_required)
    def post(self, request):
        if 'toggle' in request.POST:
            task = MainTask.objects.get(id=int(request.POST['task']), patient__user_id=request.user.id)
            if task.completed:
                task.completed = False
            else:
                task.completed = True
            task.completed_on = datetime.now()
            task.save()
            tasks = MainTask.objects.filter(patient__user_id=request.user.id, completed=False).order_by('created')[
                    :MAX_ROWS]
            return HttpResponse(json.dumps(
                {'state': task.completed,
                 'tasks': [task.as_dict() for task in tasks]
                 }))


@login_required()
def dashboard(request):
    if request.user.userprofile.is_therapist:
        return therapist_home(request)
    else:
        return PatientHomeView.as_view()(request)


@login_required()
def patient_list(request):
    client_list = Client.objects.filter(therapist__user_profile__user_id=request.user.id)
    paginator = Paginator(client_list, MAX_ROWS)
    try:
        clients = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)
    return render(request, 'therapist/patient-list.html',
                  {'clients': clients,
                   'paginator': paginator})
