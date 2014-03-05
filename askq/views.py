from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from askq.models import Proj, Ask, Answer
from askq.forms import ProjForm


def index(request):
    if 'projectname' in request.GET:
        if request.GET['projectname'] == '':
            return HttpResponseRedirect("/call/")
        else:
            if 'cur_quest' in request.GET:
                prname = request.GET['projectname']
                cur_quest = request.GET['cur_quest']
                askq = Ask.objects.filter(proj=prname)
                answers = Answer.objects.get(ask_id=cur_quest)
                projects = Proj.objects.all()
                cur_proj = Proj.objects.get(id=prname)
                form = ProjForm()
                form.fields['projectname'].initial = prname
                context = {'form': form , 'projects': projects, 'askq': askq, 'cur_proj': cur_proj, 'cur_quest': cur_quest, 'answer': answers}
                return render(request, 'askq/index.html', context)
            else:
                prname = request.GET['projectname']
                askq = Ask.objects.filter(proj=prname)
                projects = Proj.objects.all()
                cur_proj = Proj.objects.get(id=prname)
                form = ProjForm()
                form.fields['projectname'].initial = prname
                context = {'form': form , 'projects': projects, 'askq': askq, 'cur_proj': cur_proj}
                return render(request, 'askq/index.html', context)
    else:
        projects = Proj.objects.all()
        form = ProjForm()
        context = {'form': form , 'projects': projects }
        return render(request, 'askq/index.html', context)


class Asks(DetailView):
    model = Ask
    template_name = 'askq/detail.html'

