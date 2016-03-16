# coding=utf-8
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.shortcuts import render

from diagnostic.bdi_survey import get_qa_set, store_bdi_response, calculate_bdi_score, BDI_QUESTIONS


def bdi_survey_pagination(request):
    if request.method == 'POST':
        qa_set = store_bdi_response(request.user.id, request.POST['answer'])
        if qa_set is not None:
            return render(request, 'diagnostic/bdi-pagination.html',
                          {'qa_set': qa_set,
                           'progress': (qa_set[0].order / float(BDI_QUESTIONS)) * 100})
        else:
            return HttpResponseRedirect(reverse('diagnostic:bdi_score'))
    else:
        qa_set = get_qa_set(request.user.id)
        if qa_set is not None:
            return render(request, 'diagnostic/bdi-pagination.html',
                          {'qa_set': qa_set,
                           'progress': (qa_set[0].order / float(BDI_QUESTIONS)) * 100})
        else:
            return HttpResponseRedirect(reverse('diagnostic:bdi_score'))


def index(request):
    return render(request, 'diagnostic/index.html', {})


def bdi_score(request):
    return render(request, 'diagnostic/bdi_score.html',
                  {'score': calculate_bdi_score(request.user.id)})
