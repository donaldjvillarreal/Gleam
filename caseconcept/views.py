# coding=utf-8
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from caseconcept.forms import PlannerForm

from caseconcept.case_options import FREQUENCY_CHOICES, SEVERITY_CHOICES, goal_frequencies
from caseconcept import models


@login_required()
def case_index(request):
    if models.ProblemAspect.objects.filter(user=User.objects.get(id=request.user.id)).exists():
        welcome = False
    else:
        welcome = True
    return render(request, 'caseconcept/case-problem.html', {'welcome': welcome,
                                                            'frequencyOptions': FREQUENCY_CHOICES,
                                                            'severityOptions': SEVERITY_CHOICES})


@login_required()
def case_problem(request):
    if request.method == 'POST':
        problem, created = models.ProblemAspect.objects.get_or_create(user=User.objects.get(id=request.user.id),
                                                                      text=request.POST['text'],
                                                                      frequency=int(request.POST['frequency']),
                                                                      severity=int(request.POST['severity']))
        return render(request, 'caseconcept/case-problem-descriptions.html', {'problem': problem,
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
            return render(request, 'caseconcept/case-problem-summary.html', {'problems': problems})
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
        return render(request, 'caseconcept/case-goals.html',
                      {'problems': models.ProblemAspect.objects.filter(improve=True)[:3],
                       'frequencies': goal_frequencies})


@login_required()
def case_goals_rank(request):
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
        return render(request, 'caseconcept/case-goals-rank.html',
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


def index(request):
    return render(request, 'diagnostic/index.html', {})


@login_required
def cal(request):
    if request.method == 'POST':

        for slot in request.POST.getlist('WeekdayTime'):
            planner_form = PlannerForm({'WeekdayTime': slot})

            if planner_form.is_valid():

                planner = planner_form.save(commit=False)
                planner.user = request.user
                planner.save()

            else:
                print planner_form.errors

        return HttpResponseRedirect("/")

    else:
        planner_form = PlannerForm()

    return render(request, 'caseconcept/planner.html', {'planner_form': planner_form})
