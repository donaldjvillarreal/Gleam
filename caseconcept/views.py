from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from caseconcept.forms import PlannerForm

# Create your views here.
@login_required
def cal(request):
	if request.method == 'POST':

		for slot in request.POST.getlist('WeekdayTime'):
			planner_form = PlannerForm(request.POST)

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