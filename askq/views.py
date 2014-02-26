from django.shortcuts import render_to_response, RequestContext
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

def index(request):
    form = ProjForm(request.GET)
    if form.is_valid():
        form.save()
    context = dict(form=form)
    return render_to_response('askq\index.html', context)