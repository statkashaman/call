# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from askq.models import Proj, Ask, Answer
from askq.forms import ProjForm


def index(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if 'projectname' in request.GET:
            prname = request.GET['projectname']
            lq = q.split()
            qs = Q()
            for i in lq:
                qs.add(Q(['question__icontains', i]), 'AND')
            sq = Ask.objects.filter(qs).filter(proj=prname)
            cur_proj = Proj.objects.get(id=prname)
            form = ProjForm()
            form.fields['projectname'].initial = prname
            context = {'form': form,'sq': sq, 'query': q, 'cur_proj': cur_proj}
        else:
            lq = q.split()
            qs = Q()
            for i in lq:
                qs.add(Q(['question__icontains', i]),'AND')
            sq = Ask.objects.filter(qs)
            form = ProjForm()
            context = {'form': form,'sq': sq, 'query': q}
        return render(request,'askq/index.html',context)
    else:
        if 'projectname' in request.GET:
            if request.GET['projectname'] == '':
                return HttpResponseRedirect("/call/")
            else:
                if 'cur_quest' in request.GET:
                    prname = request.GET['projectname']
                    cur_quest = request.GET['cur_quest']
                    askq = Ask.objects.filter(proj=prname)
                    cur_ask = Ask.objects.get(id=cur_quest)
                    try:
                        answers = Answer.objects.get(ask_id=cur_quest)
                    except ObjectDoesNotExist:
                        answers = "К сожалению пока нету ответа"
                    cur_proj = Proj.objects.get(id=prname)
                    form = ProjForm()
                    form.fields['projectname'].initial = prname
                    context = {'form': form , 'askq': askq, 'cur_proj': cur_proj, 'cur_quest': cur_quest, 'answer': answers,'cur_ask': cur_ask}
                else:
                    prname = request.GET['projectname']
                    askq = Ask.objects.filter(proj=prname)
                    cur_proj = Proj.objects.get(id=prname)
                    form = ProjForm()
                    form.fields['projectname'].initial = prname
                    context = {'form': form , 'askq': askq, 'cur_proj': cur_proj}
            return render(request, 'askq/index.html', context)
        else:
            form = ProjForm()
            context = {'form': form}
    return render(request, 'askq/index.html', context)
