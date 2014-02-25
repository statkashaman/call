from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from askq.models import Proj
from askq.forms import ProjForm

class Projects(ListView):
    model = Proj
    context_object_name = 'projects'
    template_name = 'askq\index.html'

class DetailView(DetailView):
    model = Proj
    template_name = 'askq\detail.html'
