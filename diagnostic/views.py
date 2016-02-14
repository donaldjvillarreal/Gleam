# coding=utf-8
from django.shortcuts import render
from diagnostic import models


def hamd_survey(request):
    if request.method == 'POST':
        print request.POST
    qa_list = []
    for question in models.Question.objects.filter(survey=1).order_by('order'):
        qa_list.append((question, models.Answer.objects.filter(question=question.pk).order_by('value')))
    return render(request, 'hamd.html', {'qa_list': qa_list})
