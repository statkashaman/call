# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from askq.models import Proj, Ask, Answer, Stats
from askq.forms import ProjForm
import datetime
import xlwt

def forma(a):
    form = ProjForm()
    form.fields['projectname'].initial = a
    return(form)

def poisk(a,*args):
    lq = a.split()
    qs = Q()
    for i in lq:
        qs.add(Q(['question__icontains', i]), 'AND')
    if args:
        sq = Ask.objects.filter(qs).filter(proj=args)
    else:
        sq = Ask.objects.filter(qs)
    return(sq)


def current_project(a):
    cur_proj = Proj.objects.get(id=a)
    return(cur_proj)

def voprosi(*args):
    askp = Ask.objects.filter(proj=args)
    return(askp)

def current_vopros(a):
     cur_ask = Ask.objects.get(id=a)
     return(cur_ask)

def otvet(*args):
    try:
        answers = Answer.objects.filter(ask_id=args)
    except ObjectDoesNotExist:
        answers = "К сожалению пока нету ответа"
    return(answers)

def stats(a):
    date_now = datetime.date.today()
    da = Stats(ask_id = a, date_ask = date_now)
    da.save()

def index(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if 'projectname' in request.GET:
            prname = request.GET['projectname']
            if 'cur_ask' in request.GET:
                cur_ask = request.GET['cur_ask']
                stats(cur_ask)
                context = {'form': forma(prname),'sq': poisk(q,prname), 'query': q, 'cur_proj': current_project(prname),'cur_ask': current_vopros(cur_ask), 'answer': otvet(cur_ask)}
            else:
                context = {'form': forma(prname),'sq': poisk(q,prname), 'query': q, 'cur_proj': current_project(prname)}
        else:
            if 'cur_ask' in request.GET:
                prname = request.GET['project']
                cur_ask = request.GET['cur_ask']
                stats(cur_ask)
                context = {'form': forma(prname),'sq': poisk(q), 'query': q, 'cur_ask': current_vopros(cur_ask), 'answer': otvet(cur_ask),'cur_search_proj':current_project(prname)}
            else:
                context = {'form': forma(0),'sq': poisk(q), 'query': q}
    else:
        if 'projectname' in request.GET:
            if request.GET['projectname'] == '':
                return HttpResponseRedirect("/call/")
            else:
                prname = request.GET['projectname']
                if 'cur_ask' in request.GET:
                    cur_ask = request.GET['cur_ask']
                    stats(cur_ask)
                    context = {'form': forma(prname) , 'askp': voprosi(prname), 'cur_proj': current_project(prname), 'answer': otvet(cur_ask),'cur_ask': current_vopros(cur_ask)}
                else:
                    context = {'form': forma(prname) , 'askp': voprosi(prname), 'cur_proj': current_project(prname)}
        else:
            context = {'form': forma(0)}
    return render(request, 'askq/index.html', context)

def statistics(request):

    return render(request, 'askq/statistics.html', context)


