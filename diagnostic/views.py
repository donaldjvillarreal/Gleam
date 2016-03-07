# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from diagnostic import models
from diagnostic.case_options import FREQUENCY_CHOICES, SEVERITY_CHOICES, goal_frequencies

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
    if models.ProblemAspect.objects.filter(user=User.objects.get(id=request.user.id)).exists():
        welcome = False
    else:
        welcome = True
    return render(request, 'diagnostic/case-problem.html', {'welcome': welcome,
                                                            'frequencyOptions': FREQUENCY_CHOICES,
                                                            'severityOptions': SEVERITY_CHOICES})


@login_required()
def case_problem(request):
    if request.method == 'POST':
        problem, created = models.ProblemAspect.objects.get_or_create(user=User.objects.get(id=request.user.id),
                                                                      text=request.POST['text'],
                                                                      frequency=int(request.POST['frequency']),
                                                                      severity=int(request.POST['severity']))
        return render(request, 'diagnostic/case-problem-descriptions.html', {'problem': problem,
                                                                             'distressLevels': range(0, 11)})
    else:
        return HttpResponseRedirect(reverse('diagnostic:case_index'))


@login_required()
def case_problem_description(request):
    if request.method == 'POST':
        problem_description, created = models.ProblemAspectSituation.objects.get_or_create(
            problem=models.ProblemAspect.objects.get(id=request.POST['problem']),
            situation=request.POST['situationInput1'],
            thought=request.POST['thoughtInput1'],
            feeling=request.POST['feelingInput1'],
            reaction=request.POST['reactionInput1'],
            distress_level=request.POST['distressInput1'])
        problem_description_2, created_2 = models.ProblemAspectSituation.objects.get_or_create(
            problem=models.ProblemAspect.objects.get(id=request.POST['problem']),
            situation=request.POST['situationInput2'],
            thought=request.POST['thoughtInput2'],
            feeling=request.POST['feelingInput2'],
            reaction=request.POST['reactionInput2'],
            distress_level=request.POST['distressInput2'])
        if request.GET.get('previous', None) is not None:
            return HttpResponseRedirect(reverse('diagnostic:case_index'))
        else:
            return HttpResponseRedirect(reverse('diagnostic:case_problem_summary'))
    else:
        return HttpResponseRedirect(reverse('diagnostic:case_index'))


@login_required()
def case_problem_summary(request):
    if request.method == 'POST':
        for problem_id in request.POST.getlist('problems[]'):
            problem = models.ProblemAspect.objects.get(id=int(problem_id))
            problem.improve = True
            problem.save()
        if len(request.POST.getlist('problems[]')) >= 1:
            return HttpResponseRedirect(reverse('diagnostic:case_goals'))
        else:
            # TODO: Route to calendar
            return HttpResponseRedirect(reverse('diagnostic:case_index'))
    else:
        problems = models.ProblemAspect.objects.filter(user=User.objects.get(id=request.user.id))
        if len(problems) > 1:
            return render(request, 'diagnostic/case-problem-summary.html', {'problems': problems})
        elif len(problems) == 1:
            return HttpResponseRedirect(reverse('diagnostic:case_goals'))
        else:
            # TODO: Route to calendar
            return HttpResponseRedirect(reverse('diagnostic:case_index'))


@login_required()
def case_goals(request):
    # Check if any problem aspects improve = True, if not, set first to improve
    if not models.ProblemAspect.objects.filter(improve=True).exists():
        problems = models.ProblemAspect.objects.all()
        if len(problems) > 0:
            problem = problems[0]
            problem.improve = True
            problem.save()
        else:
            return HttpResponseRedirect(reverse('diagnostic:case_index'))
    if request.method == 'POST':
        # Get the first three problems that have been marked as improve = True
        problems = models.ProblemAspect.objects.filter(improve=True)[:3]
        for problem in problems:
            models.ProblemGoal.objects.get_or_create(
                user=User.objects.get(id=request.user.id),
                problem=models.ProblemAspect.objects.get(id=problem.id),
                action=request.POST['%i-action' % problem.id],
                frequency=int(request.POST['%i-frequency' % problem.id]))
        if len(problems) >= 2:
            return HttpResponseRedirect(reverse('diagnostic:case_goals_rank'))
        else:
            # Only 1 problem area specified, skip to calendar
            # TODO: Route to calendar
            return HttpResponseRedirect(reverse('diagnostic:case_index'))
    else:
        return render(request, 'diagnostic/case-goals.html',
                      {'problems': models.ProblemAspect.objects.filter(improve=True)[:3],
                       'frequencies': goal_frequencies})


@login_required()
def case_goals_rank(request):
    if request.method == 'POST':
        # Get list of goals
        goals = request.POST.getlist('goals[]')
        goals[0] = models.ProblemGoal.objects.get(id=goals[0])
        if len(goals) < 3:
            # lets us create the objects if less than 3 problems were given
            if len(goals) == 2:
                goals[1] = models.ProblemGoal.objects.get(id=goals[1])
                goals.append(None)
            else:
                goals.append(None)
                goals.append(None)
        ranking, created = models.ProblemGoalRanking.objects.get_or_create(user=User.objects.get(id=request.user.id),
                                                                           first=goals[0],
                                                                           second=goals[1],
                                                                           third=goals[2],
                                                                           current_goal=goals[0])
        return render(request, 'diagnostic/case-goal-confirm.html',
                      {'ranking': ranking})
    else:
        return render(request, 'diagnostic/case-goals-rank.html',
                      {'goals': models.ProblemGoal.objects.filter(user=User.objects.get(id=request.user.id))[:3]})


@login_required()
def case_goal_rank_confirm(request):
    if request.method == 'POST':
        ranking = models.ProblemGoalRanking.objects.get(id=int(request.POST['rankId']))
        ranking.current_goal = models.ProblemGoal.objects.get(id=int(request.POST['goal']))
        ranking.save()
        # TODO: route to calendar
        return HttpResponseRedirect(reverse('diagnostic:case_index'))
    else:
        return HttpResponseRedirect(reverse('diagnostic:case_goals_rank'))
