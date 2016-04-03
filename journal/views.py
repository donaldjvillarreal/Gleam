# coding=utf-8
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from alchemyapi.alchemyapi import AlchemyAPI

from journal import forms

# Create your views here.
@login_required
def journalEntry(request):
	user = User.objects.get(id=request.user.id)
	#alchemyapi = AlchemyAPI()
	#myText = "I'm excited to get started with AlchemyAPI!"
	#response = alchemyapi.sentiment("text", myText)
	#print(response)
	#print("Sentiment: ", response["docSentiment"]["type"])
	if request.method == 'POST':
		entry_form = forms.entryForm(data=request.POST)
		if entry_form.is_valid():
			journal_entry = entry_form.save(commit=False)
			journal_entry.user = user
			#myText = request.POST.get('entry'):
			#journal.response = alchemyapi.sentiment("text", myText)
			journal_entry.save()
			#HttpResponseRedirect(reverse('course:start_course'))
		else:
			print entry_form.errors
	else:
	    entry_form = forms.entryForm()
	return render(request, 'journal/entry.html', {'entry_form': entry_form})

