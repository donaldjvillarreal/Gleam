from django import forms
from django.contrib.auth.models import User
from caseconcept.models import PracticeCal

class PlannerForm(forms.ModelForm):
    class Meta:
        model = PracticeCal
        fields = ('WeekdayTime',)