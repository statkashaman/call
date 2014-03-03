# coding=utf-8
from django import forms
from models import Proj

class ProjForm(forms.ModelForm):
    projectname = forms.ModelChoiceField(queryset = Proj.objects.all(),empty_label="Выберите проект",widget=forms.Select(attrs={'class':'dropdown'}),label="Проекты")
    class Meta:
        model = Proj
        fields = ('projectname',)