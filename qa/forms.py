from qa.models import *
from django.contrib.auth.models import User
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text', 'tags')
