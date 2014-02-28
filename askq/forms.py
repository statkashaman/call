# coding=utf-8
from django import forms
from models import Proj

class ProjForm(forms.ModelForm):
    class Meta:
        model = Proj
        fields = ('projectname',)
        widgets = {
            'projectname': forms.Select(choices = Proj.objects.all()),
        }
