from django.shortcuts import render
from tasks import forms
from django.contrib.auth.decorators import login_required
from authenticate.models import Client, Therapist, UserProfile
from tasks.models import TaskGroup

# Create your views here.
@login_required
def CreateHomework(request):

    user_id = request.user.id
    prevhw = TaskGroup.objects.filter(therapist=Therapist.objects.get(id=user_id))
    patients = Client.objects.filter(therapist=Therapist.objects.get(id=user_id))

    if request.method == 'POST':
        hw_form = forms.CreateTaskGroup(data=request.POST)
        if hw_form.is_valid():
            patient = request.POST['patient']
            hw = hw_form.save(commit=False)
            hw.therapist = Therapist.objects.get(user_profile__user=request.user.id)
            hw.patient = UserProfile.objects.get(user_id=patient)
            hw.save()
        else:
            print hw_form.errors
    else:
        hw_form = forms.CreateTaskGroup()

    return render(request, 'tasks/CreateHW.html', {'hw_form': hw_form, 'prevhw': prevhw, 'patients': patients})