# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm


class Proj(models.Model):
    projectname = models.CharField("Имя проекта", max_length=200)
    urlp = models.URLField("Адрес проекта", max_length=200)
    class Meta:
        verbose_name = u'Проект'
        verbose_name_plural = u'Проекты'
    def __unicode__(self):
        return self.projectname


class Ask(models.Model):
    proj = models.ForeignKey(Proj,verbose_name = "Проект")
    question = models.CharField("Вопрос", max_length=200)
    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'
    def __unicode__(self):
        return self.question


class Answer(models.Model):
    ask = models.ForeignKey(Ask,verbose_name = "Вопрос")
    ans = models.TextField("Ответ")
    class Meta:
        verbose_name = u'Ответ'
        verbose_name_plural = u'Ответы'
    def __unicode__(self):
        return self.ans