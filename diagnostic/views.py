# coding=utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from diagnostic import models
from diagnostic.case_options import FREQUENCY_CHOICES, SEVERITY_CHOICES

from collections import OrderedDict


def hamd_survey(request):
    if request.method == 'GET':
        question_number = 1
    else:
        question_number = int(request.POST.get('current', 1))

    if question_number > 21:
        # calculate the total points here
        total = 0
        for value in request.session['bdi_dict'].values():
            total += int(value)
        return render(request, 'diagnostic/results.html', {'total': total})

    if question_number > 1 and request.session['hamd_dict'] is None:
        question_number = 1

    if request.session.get('hamd_dict') is None:
        request.session['hamd_dict'] = OrderedDict()

    if request.method == 'POST':
        bdi_dict = request.session['hamd_dict']
        bdi_dict[question_number - 1] = request.POST['answer']
        request.session['hamd_dict'] = bdi_dict

    question = models.Question.objects.filter(survey__short_name='HAM-D').get(order=question_number)
    qa_set = (question, models.Answer.objects.filter(question=question.pk).order_by('value'))
    return render(request, 'diagnostic/hamd-pagination.html', {'qa_set': qa_set,
                                                               'current': question_number + 1,
                                                               'progress': int((question_number / 21.0) * 100)})


def bdi_survey_pagination(request):
    if request.method == 'GET':
        question_number = 1
    else:
        question_number = int(request.POST.get('current', 1))

    if question_number > 21:
        total = 0
        for value in request.session['bdi_dict'].values():
            total += int(value)
        return render(request, 'diagnostic/results.html', {'total': total})

    if question_number > 1 and request.session['bdi_dict'] is None:
        question_number = 1

    if request.session.get('bdi_dict') is None:
        request.session['bdi_dict'] = OrderedDict()

    if request.method == 'POST':
        bdi_dict = request.session['bdi_dict']
        bdi_dict[question_number - 1] = request.POST['answer']
        request.session['bdi_dict'] = bdi_dict

    question = models.Question.objects.filter(survey__short_name='BDI').get(order=question_number)
    qa_set = (question, models.Answer.objects.filter(question=question.pk).order_by('value'))
    return render(request, 'diagnostic/bdi-pagination.html', {'qa_set': qa_set,
                                                               'current': question_number + 1,
                                                               'progress': int((question_number / 21.0) * 100)})


@login_required()
def case_index(request):
    return render(request, 'diagnostic/case-index.html', {'welcome': False,
                                                          'frequencyOptions': FREQUENCY_CHOICES,
                                                          'severityOptions': SEVERITY_CHOICES})
