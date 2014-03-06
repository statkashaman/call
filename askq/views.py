# coding=utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from askq.models import Proj, Ask, Answer
from askq.forms import ProjForm


def index(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        sq = Ask.objects.filter(question__icontains=q)
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
                    answers = Answer.objects.get(ask_id=cur_quest)
                    cur_proj = Proj.objects.get(id=prname)
                    form = ProjForm()
                    form.fields['projectname'].initial = prname
                    context = {'form': form , 'askq': askq, 'cur_proj': cur_proj, 'cur_quest': cur_quest, 'answer': answers,'cur_ask': cur_ask}
                    return render(request, 'askq/index.html', context)
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
