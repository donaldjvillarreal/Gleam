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

BDI_QUESTIONS_LENGTH = len(models.Question.objects.filter(survey__short_name='BDI'))
bdi_survey = models.Survey.objects.get(short_name='BDI')


def get_qa_set(session_key):
    session = Session.objects.get(session_key=session_key)
    survey_set = models.SurveySet.objects.filter(session=session)
    if survey_set.exists():
        survey_set = survey_set.order_by('-last_modified').first()
        question_set = []
        for answer in survey_set.answers.all():
            question_set.append(answer.question)
        if len(question_set) == BDI_QUESTIONS_LENGTH:
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
    if len(survey_set.answers.all()) == BDI_QUESTIONS_LENGTH:
        survey_set.completed_on = timezone.localtime(timezone.now())
        survey_set.save()
        return None
    else:
        question = models.Question.objects.get(survey=bdi_survey, order=(answer.question.order + 1))
        return question, models.Answer.objects.filter(question=question)


def calculate_bdi_score(session_key):
    session = Session.objects.get(session_key=session_key)
    answers = models.SurveySet.objects.filter(session=session).order_by('-last_modified').first().answers.all()
    total_score, emotion_score, thought_score, behavior_score, physical_score = 0, 0, 0, 0, 0
    # Since question 9 was replaced and not removed in the database, questions >= 9 in BDI Analysis doc is decremented
    emotion_list = [1, 2, 3, 5, 6, 7, 8, 9, 10, 19]
    thought_list = [2, 3, 7, 8, 12, 13, 19]
    behavior_list = [4, 9, 11, 13, 14]
    physical_list = [14, 15, 16, 17, 18, 19, 20]
    for answer in answers:
        total_score += answer.value
        # calculate course ratios
        question_order = answer.question.order
        if question_order in emotion_list:
            emotion_score += 1
        elif question_order in thought_list:
            thought_score += 1
        elif question_order in behavior_list:
            behavior_score += 1
        elif question_order in physical_list:
            physical_score += 1
    return {'total_score': total_score,
            'emotion_score': emotion_score,
            'thought_score': thought_score,
            'behavior_score': behavior_score,
            'physical_score': physical_score}
