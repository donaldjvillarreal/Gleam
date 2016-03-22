# coding=utf-8
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from caseconcept import forms
from caseconcept.case_options import FREQUENCY_CHOICES, SEVERITY_CHOICES, goal_frequencies, DEFAULT_PROBLEMS
from caseconcept import models


def clean_stale_problems(user_id):
    problems = models.ProblemAspect.objects.filter(user=User.objects.get(id=user_id))
    # Check if problem situation exists for problem, if not, delete.
    for problem in problems:
        if not models.ProblemAspectSituation.objects.filter(problem=problem).exists():
            problem.delete()
    return problems


@login_required()
def case_index(request):
    problems = clean_stale_problems(request.user.id)
    if problems.exists():
        welcome = False
        texts = [problem.text for problem in problems]
    else:
        welcome = True
        texts = None
    return render(request, 'caseconcept/case-problem.html',
                  {'welcome': welcome,
                   'frequencyOptions': FREQUENCY_CHOICES,
                   'severityOptions': SEVERITY_CHOICES,
                   'error': request.GET.get('formIssue', False),
                   'texts': texts,
                   'default_problems': DEFAULT_PROBLEMS,
                   'custom_problems': [problem.text for problem in problems if problem.text not in DEFAULT_PROBLEMS]})


@login_required()
def case_problem(request):
    if request.method == 'POST':
        problem_form = forms.ProblemAspectForm({'text': request.POST['text'],
                                                'frequency': int(request.POST['frequency']),
                                                'severity': int(request.POST['severity'])})
        if problem_form.is_valid():
            problem = problem_form.save(commit=False)
            problem.user = User.objects.get(id=request.user.id)
            problem.save()
            return render(request, 'caseconcept/case-problem-descriptions.html', {'problem': problem,
                                                                                  'distressLevels': range(0, 6)})
        else:
            clean_stale_problems(request.user.id)
            return HttpResponseRedirect('%s?formIssue=True' % reverse('case:index'))
    else:
        return HttpResponseRedirect(reverse('case:index'))


@login_required()
def case_problem_description(request):
    if request.method == 'POST':
        errors_1, errors_2 = None, None
        problem_id = request.POST['problem']
        problem_aspect = models.ProblemAspect.objects.get(id=problem_id)
        problem_description_form = forms.ProblemAspectSituationForm({
            'summary': request.POST['summary'],
            'situation': request.POST['situationInput1'],
            'thoughts_and_feelings': request.POST['thoughtFeelingInput1'],
            'reaction': request.POST['reactionInput1'],
            'distress_level': request.POST['distressInput1']})
        if problem_description_form.is_valid():
            problem_description = problem_description_form.save(commit=False)
            problem_description.problem = problem_aspect
            problem_description.save()
        else:
            errors_1 = problem_description_form.errors

        if request.POST['situationInput2']:
            problem_description_form_2 = forms.ProblemAspectSituationForm({
                'summary': request.POST['summary'],
                'problem': problem_aspect,
                'situation': request.POST['situationInput2'],
                'thoughts_and_feelings': request.POST['thoughtFeelingInput1'],
                'reaction': request.POST['reactionInput2'],
                'distress_level': request.POST['distressInput2']})
            if problem_description_form_2.is_valid():
                problem_description = problem_description_form_2.save(commit=False)
                problem_description.problem = problem_aspect
                problem_description.save()
            else:
                errors_2 = problem_description_form_2.errors

        if errors_1 is not None or errors_2 is not None:
            # Some form errors, display them
            return render(request, 'caseconcept/case-problem-descriptions.html',
                          {'problem': models.ProblemAspect.objects.get(id=request.POST['problem']),
                           'distressLevels': range(0, 6),
                           'errors_1': errors_1,
                           'errors_2': errors_2})

        elif request.GET.get('previous', None) is not None:
            # No errors, go to index if needed
            return HttpResponseRedirect(reverse('case:index'))
        else:
            # Done with problems, go to problem description
            return HttpResponseRedirect(reverse('case:problem_summary'))

    else:
        return HttpResponseRedirect(reverse('case:index'))


@login_required()
def case_problem_summary(request):
    if request.method == 'POST':
        for problem in models.ProblemAspect.objects.filter(improve=True):
            problem.improve = False
            problem.save()
        for problem_id in request.POST.getlist('problems[]'):
            problem = models.ProblemAspect.objects.get(id=int(problem_id))
            problem.improve = True
            problem.save()
        return HttpResponseRedirect(reverse('case:goals'))
    else:
        problems = models.ProblemAspect.objects.filter(user=User.objects.get(id=request.user.id))
        if len(problems) > 1:
            return render(request, 'caseconcept/case-problem-summary.html', {'problems': problems})
        elif len(problems) == 1:
            return HttpResponseRedirect(reverse('case:goals'))
        else:
            return HttpResponseRedirect(reverse('case:calendar'))


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
            return HttpResponseRedirect(reverse('case:index'))
    else:
        # Get the first three problems that have been marked as improve = True
        problems = models.ProblemAspect.objects.filter(improve=True)
        if len(problems) > 1:
            problems = problems.order_by('-created')[:3]
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        for problem in problems:
            frequency = int(request.POST['%i-frequency' % problem.id])
            # Check if goals with unique columns exists, if so, delete them and create new one with updated info
            goals = models.ProblemGoal.objects.filter(user=user,
                                                      problem=problem.id,
                                                      frequency=frequency)
            if goals.exists():
                for goal in goals:
                    goal.delete()

            models.ProblemGoal.objects.create(user=user,
                                              problem=models.ProblemAspect.objects.get(id=problem.id),
                                              action=request.POST['%i-action' % problem.id],
                                              frequency=frequency,
                                              stale=False)
        if len(problems) >= 2:
            return HttpResponseRedirect(reverse('case:goals_rank'))
        else:
            first_goal = models.ProblemGoal.objects.filter(user=User.objects.get(id=request.user.id)).first()
            models.ProblemGoalRanking.objects.get_or_create(user=User.objects.get(id=request.user.id),
                                                            first=first_goal,
                                                            second=None,
                                                            third=None,
                                                            current_goal=first_goal)
            return HttpResponseRedirect(reverse('case:calendar'))
    else:
        return render(request, 'caseconcept/case-goals.html',
                      {'problems': problems,
                       'frequencies': goal_frequencies})


@login_required()
def case_goals_rank(request):
    if not models.ProblemAspect.objects.all().exists():
        return HttpResponseRedirect(reverse('case:index'))
    if request.method == 'POST':
        # Get list of goals
        goals = request.POST.getlist('goals[]')
        goals[0] = models.ProblemGoal.objects.get(id=int(goals[0]))
        if len(goals) <= 3:
            # lets us create the objects if less than 3 problems were given
            if len(goals) == 3:
                goals[1] = models.ProblemGoal.objects.get(id=int(goals[1]))
                goals[2] = models.ProblemGoal.objects.get(id=int(goals[2]))
            elif len(goals) == 2:
                goals[1] = models.ProblemGoal.objects.get(id=int(goals[1]))
                goals.append(None)
            else:
                goals.append(None)
                goals.append(None)
        ranking, created = models.ProblemGoalRanking.objects.get_or_create(user=User.objects.get(id=request.user.id),
                                                                           first=goals[0],
                                                                           second=goals[1],
                                                                           third=goals[2],
                                                                           current_goal=goals[0])
        return render(request, 'caseconcept/case-goal-confirm.html',
                      {'ranking': ranking})
    else:
        goals = models.ProblemGoal.objects.filter(user=User.objects.get(id=request.user.id), stale=False).order_by(
            '-created')[:3]
        return render(request, 'caseconcept/case-goals-rank.html',
                      {'goals': goals})


@login_required()
def case_goal_rank_confirm(request):
    if request.method == 'POST':
        ranking = models.ProblemGoalRanking.objects.get(id=int(request.POST['rankId']))
        ranking.current_goal = models.ProblemGoal.objects.get(id=int(request.POST['goal']))
        ranking.save()
        return HttpResponseRedirect(reverse('case:calendar'))
    else:
        return HttpResponseRedirect(reverse('case:goals_rank'))


@login_required
def calendar(request):
    user = User.objects.get(id=request.user.id)
    if 'goal' in request.GET:
        # Check if updating calendar weekday_time
        goal = models.ProblemGoalRanking.objects.get(user=user,
                                                     first=models.ProblemGoal.objects.get(id=request.GET['goal']))
    else:
        goal = models.ProblemGoalRanking.objects.filter(user=user).order_by('-created')[0]
    if request.method == 'POST':
        for slot in request.POST.getlist('weekday_time'):
            planner_form = forms.PlannerForm({'day': int(slot[0]),
                                              'hour': int(slot[1:3]),
                                              'minute': int(slot[3:5])})
            if planner_form.is_valid():
                planner = planner_form.save(commit=False)
                planner.goal = goal.current_goal
                planner.save()
            else:
                print planner_form.errors
        if 'goal' in request.GET:
            return HttpResponseRedirect(reverse('case:start_course'))
        else:
            return HttpResponseRedirect(u'%s?courses=True' % reverse('core:progress_check'))

    else:
        # Delete if instance of practice calendar exists (good for updating weekday_time)
        if models.PracticeCalendar.objects.filter(goal=goal.current_goal).exists():
            for practice_calendar in models.PracticeCalendar.objects.filter(goal=goal.current_goal):
                practice_calendar.delete()
        planner_form = forms.PlannerForm()

    return render(request, 'caseconcept/planner.html', {'planner_form': planner_form,
                                                        'goal': goal})


@login_required()
def start_course(request):
    return render(request, 'caseconcept/start-course.html',
                  {'slots': models.PracticeCalendar.objects.filter(goal__user=User.objects.get(id=request.user.id))})
