from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from askq.models import Proj, Ask
from askq.forms import ProjForm


def index(request):
        projects = Proj.objects.all()
        form = ProjForm
        context = {'form': form , 'projects': projects}
        return render(request, 'askq/index.html', context)


class Asks(DetailView):
    model = Ask
    template_name = 'askq/detail.html'

