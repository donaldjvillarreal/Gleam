# coding=utf-8
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import requests
#from alchemyapi.alchemyapi import AlchemyAPI

from journal import forms, models

# Create your views here.
@login_required
def journalEntry(request):
    user = User.objects.get(id=request.user.id)
    textSentiment = 'http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment'
    keywordExtraction = 'http://gateway-a.watsonplatform.net/calls/text/TextGetRankedKeywords'
    entityExtraction = 'http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities'
    key = 'fe9480c1e35a7ade844fa82699c8d7e6792f14bb'
    if request.method == 'POST':
        entry_form = forms.entryForm(data=request.POST)
        if entry_form.is_valid():
            journal_entry = entry_form.save(commit=False)
            journal_entry.user = user
            myText = request.POST.get('entry')
            tdata = requests.get(textSentiment, {'apikey': key, 'text': myText, 'outputMode': 'json'})
            tresponse = tdata.json()
            journal_entry.sentimentType = tresponse['docSentiment']['type']
            journal_entry.sentimentScore = tresponse['docSentiment']['score']
            journal_entry.save()

            #Keyword Extraction
            kdata = requests.get(keywordExtraction, {'apikey': key, 'text': myText, 'outputMode': 'json', 'sentiment': 1})
            kresponse = kdata.json()
            print kresponse
            for keyword in kresponse['keywords']:
                if keyword['sentiment']['type'] == 'neutral':
                    keyScore = 0
                else:
                    keyScore = keyword['sentiment']['score']
                models.keywords.objects.create(entry=journal_entry,
                                               text=keyword['text'],
                                               relevance=keyword['relevance'],
                                               sentimentType=keyword['sentiment']['type'],
                                               sentimentScore=keyScore)

            #Entity Extraction
            edata = requests.get(entityExtraction, {'apikey': key, 'text': myText, 'outputMode': 'json', 'sentiment': 1})
            eresponse = edata.json()
            print eresponse
            for entity in eresponse['entities']:
                if entity['entity']['sentiment']['type'] == 'neutral':
                    entScore = 0
                else:
                    entScore = entity['entity']['sentiment']['type']
                models.entities.objects.create(entry = journal_entry,
                                               type = entity['entity']['entityType'],
                                               relevance = entity['entity']['relevance'],
                                               count = entity['entity']['count'],
                                               text = entity['entity']['text'],
                                               sentimentType = entity['entity']['sentiment']['type'],
                                               sentimentScore = entScore)
            #HttpResponseRedirect(reverse('course:start_course'))
        else:
            print entry_form.errors
        
    else:
        entry_form = forms.entryForm()
    return render(request, 'journal/entry.html', {'entry_form': entry_form})

