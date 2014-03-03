from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from askq.models import Proj, Ask
from askq.forms import ProjForm


def index(request):
    if 'projectname' in request.GET:
        prname = request.GET['projectname']
        askq = Ask.objects.filter(proj=prname)
        askqs = Ask.objects.all()
        projects = Proj.objects.all()
        cur_proj = Proj.objects.filter(id=prname)
        form = ProjForm()
        context = {'form': form , 'projects': projects, 'askq': askq, 'askqs': askqs, 'cur_proj': cur_proj}
        return render(request, 'askq/index.html', context)
    else:
        projects = Proj.objects.all()
        form = ProjForm()
        context = {'form': form , 'projects': projects }
        return render(request, 'askq/index.html', context)


class Asks(DetailView):
    model = Ask
    template_name = 'askq/detail.html'

