from django.shortcuts import render_to_response, RequestContext
from django.views.generic import ListView, DetailView
from askq.models import Proj, Ask
from askq.forms import ProjForm

class Projects(ListView):
    model = Proj
    context_object_name = 'projects'
    template_name = 'askq/index.html'
    def index(request):
        return render_to_response('askq/index.html', {'form':ProjForm()}, context_instance=RequestContext(request))


class Asks(DetailView):
    model = Ask
    template_name = 'askq/detail.html'

