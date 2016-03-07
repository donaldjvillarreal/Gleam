from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from caseconcept.forms import PlannerForm

# Create your views here.
@login_required
def cal(request):
	if request.method == 'POST':
		planner_form = PlannerForm(request.POST)

		if planner_form.is_valid():
			planner = planner_form.save(commit=False)
			planner.user = request.user
			WeekdayTime = request.POST.getlist('WeekdayTime')
			for slot in WeekdayTime:
				planner.WeekdayTime = slot
				print slot
				planner.save()

			return HttpResponseRedirect("/")

		else:
			print planner_form.errors

	else:
		planner_form = PlannerForm()

	return render(request, 'caseconcept/planner.html', {'planner_form': planner_form})