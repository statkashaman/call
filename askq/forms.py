# coding=utf-8
from django import forms
from models import Proj

class ProjForm(forms.ModelForm):
   class Meta:
       model = Proj
