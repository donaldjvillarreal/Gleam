# coding=utf-8
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from journal import forms, models

# Create your views here.
@login_required
def entry(request):
    user = User.objects.get(id=request.user.id)
    textSentiment = 'http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment'
    keywordExtraction = 'http://gateway-a.watsonplatform.net/calls/text/TextGetRankedKeywords'
    # entityExtraction = 'http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities'
    key = 'fe9480c1e35a7ade844fa82699c8d7e6792f14bb'
    if request.method == 'POST':
        entry_form = forms.EntryForm(data=request.POST)

        if entry_form.is_valid():
            journal_entry = entry_form.save(commit=False)
            journal_entry.user = user
            myText = request.POST.get('entry')
            tdata = requests.get(textSentiment, {'apikey': key, 'text': myText, 'outputMode': 'json'})
            tresponse = tdata.json()
            journal_entry.sentiment_type = tresponse['docSentiment']['type']
            if tresponse['docSentiment']['type'] == 'neutral':
                journal_entry.sentiment_score = 0
            else:
                journal_entry.sentiment_score = tresponse['docSentiment']['score']
            journal_entry.save()

            # Keyword Extraction
            kdata = requests.get(keywordExtraction,
                                 {'apikey': key, 'text': myText, 'outputMode': 'json', 'sentiment': 1})
            kresponse = kdata.json()

            for keyword in kresponse['keywords']:
                if keyword['sentiment']['type'] == 'neutral':
                    keyScore = 0
                else:
                    keyScore = keyword['sentiment']['score']
                models.Keywords.objects.create(entry=journal_entry,
                                               text=keyword['text'],
                                               relevance=keyword['relevance'],
                                               sentiment_type=keyword['sentiment']['type'],
                                               sentiment_score=keyScore)

                # Entity Extraction
                # edata = requests.get(entityExtraction, {'apikey': key, 'text': myText, 'outputMode': 'json', 'sentiment': 1})
                # eresponse = edata.json()
                # print eresponse
                # for entitylist in eresponse['entities']:
                #    for entity in entitylist:
                #        if entity['sentiment']['type'] == 'neutral':
                #            entScore = 0
                #        else:
                #             entScore = entity['sentiment']['type']
                #         models.entities.objects.create(entry = journal_entry,
                #                                       type = entity['entityType'],
                #                                       relevance = entity['relevance'],
                #                                       count = entity['count'],
                #                                       text = entity['text'],
                #                                       sentiment_type = entity['sentiment']['type'],
                #                                       sentiment_score = entScore)
                # HttpResponseRedirect(reverse('course:start_course'))
        else:
            print entry_form.errors

    else:
        entry_form = forms.EntryForm()
    return render(request, 'journal/entry.html', {'entry_form': entry_form})


@login_required
def word_list(request):
    if request.method == 'GET':
        user = User.objects.get(id=request.user.id)
        jEntry = models.Entry.objects.filter(user=user).order_by('-created')

        # list of keywords and entities in order of relevance descending
        keywords = models.Keywords.objects.filter(entry=jEntry[0])
        entity = models.Entities.objects.filter(entry=jEntry[0])
        wordlist = []
        for words in keywords:
            wordlist.append(words)
        for words in entity:
            wordlist.append(words)
        wordlist = sorted(keywords, key=lambda x: x.relevance, reverse=True)

        # list of journal entry scores for plot
        entryvalues = jEntry.order_by('created')

    else:
        wordlist = {}
        entryvalues = {}

    return render(request, 'journal/wordlist.html', {'wordlist': wordlist,
                                                     'entryvalues': entryvalues})

@login_required
def list_view(request):
    if request.method == 'GET':
        user = User.objects.get(id=request.user.id)

        entry_list = models.Entry.objects.filter(user=user).order_by('-created')
        paginator = Paginator(entry_list, 5)

        page = request.GET.get('page')

        try:
            entries = paginator.page(page)
        except PageNotAnInteger:
            entries = paginator.page(1)
        except EmptyPage:
            entries = paginator.page(paginator.num_pages)

    return render(request, 'journal/listview.html', {'entries': entries, 'paginator': paginator})