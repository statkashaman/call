from django.shortcuts import render
from django.views.generic import ListView, DetailView
from askq.models import Proj, Ask
from askq.forms import ProjForm

class Projects(ListView):
    model = Proj
    context_object_name = 'projects'
    template_name = 'askq\index.html'

class Asks(DetailView):
    model = Ask
    template_name = 'askq\detail.html'

def projlist(request):
    form = ProjForm()
    return render(request, 'askq\index.html', {'form': form })
