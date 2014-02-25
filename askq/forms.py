from django import forms
from askq.models import Proj

class ProjForm(forms.Form):
    projectname = forms.CharField(max_length=200,widget=forms.Select(choices=Proj.objects.all()))
    urlp = forms.URLField(max_length=200)

#class AskForm(forms.Form):
#    authors = forms.ModelMultipleChoiceField(queryset=Proj.objects.all())
#    name = forms.CharField(max_length=100)
