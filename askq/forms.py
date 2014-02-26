# coding=utf-8
from django import forms
from models import Proj

class ProjForm(forms.ModelForm):
    projmod = forms.ModelChoiceField(queryset=Proj.objects.all(), empty_label="Выберите проект")
    class Meta:
        model = Proj

