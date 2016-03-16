# coding=utf-8
"""
Logic for storing and present BDI survey questions, answers, and responses.

BDI scale:
0–9: indicates minimal depression
10–18: indicates mild depression
19–29: indicates moderate depression
30–63: indicates severe depression.
"""

from diagnostic import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

BDI_QUESTIONS = len(models.Question.objects.filter(survey__short_name='BDI'))
bdi_survey = models.Survey.objects.get(short_name='BDI')


def get_qa_set(session_key):
    session = Session.objects.get(session_key=session_key)
    survey_set = models.SurveySet.objects.filter(session=session)
    if survey_set.exists():
        survey_set = survey_set.order_by('-last_modified').first()
        question_set = []
        for answer in survey_set.answers.all():
            question_set.append(answer.question)
        if len(question_set) == BDI_QUESTIONS:
            # all questions answered
            survey_set.completed_on = timezone.localtime(timezone.now())
            survey_set.save()
            return None
        else:
            for question in models.Question.objects.filter(survey=bdi_survey).order_by('order'):
                if question not in question_set:
                    return question, models.Answer.objects.filter(question=question)
    else:
        models.SurveySet.objects.create(session=session, survey=bdi_survey)
        question = models.Question.objects.get(survey=bdi_survey, order=1)
        return question, models.Answer.objects.filter(question=question)


def store_bdi_response(session_key, answer_id):
    session = Session.objects.get(session_key=session_key)
    answer = models.Answer.objects.get(id=int(answer_id))
    survey_set = models.SurveySet.objects.filter(session=session).order_by('-last_modified').first()
    models.QuestionAnswerSet.objects.create(survey_set=survey_set, answer=answer)
    if len(survey_set.answers.all()) == BDI_QUESTIONS:
        survey_set.completed_on = timezone.localtime(timezone.now())
        survey_set.save()
        return None
    else:
        question = models.Question.objects.get(survey=bdi_survey, order=(answer.question.order + 1))
        return question, models.Answer.objects.filter(question=question)


def calculate_bdi_score(session_key):
    session = Session.objects.get(session_key=session_key)
    answers = models.SurveySet.objects.filter(session=session).order_by('-last_modified').first().answers.all()
    score = 0
    for answer in answers:
        score += answer.value
    return score
