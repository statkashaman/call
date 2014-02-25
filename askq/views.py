from django.views.generic import ListView, DetailView
from askq.models import Proj, Ask
from askq.forms import ProjForm

class Projects(ListView):
    model = Proj
    context_object_name = 'projects'
    template_name = 'askq\index.html'

class Asks(DetailView):
    model = Ask
    context_object_name = 'asks'
    template_name = 'askq\detail.html'
