# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from core import forms


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
