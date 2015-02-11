# -*- coding: utf-8 -*-
from django.contrib import admin
from askq.models import Proj, Ask, Answer

class AskInline(admin.TabularInline):
    model = Ask
    extra = 0
    fieldsets = [
        ( 'Вопрос', {'fields': ['question'], 'classes': ['question']}),
    ]

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1
    max_num = 1
    fieldsets = [
        ( None, {'fields': ['ans'], 'classes': ['wide']}),
    ]

class ProAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Имя поекта', {'fields': ['projectname'], 'classes': ['wide']}),
        ('Адрес проекта', {'fields': ['urlp']}),
        ('Файл проекта',{'fields': ['filetoproj']}),
    ]
    inlines = [AskInline]
    list_display = ('projectname', 'urlp')

class AskAdmin(admin.ModelAdmin):
    ordering = ('proj',)
    fieldsets = [
        ('Проект', {'fields':['proj']}),
        ('Вопрос', {'fields': ['question'],'classes': ['question']}),
        ('Файл вопроса',{'fields': ['filetoask']}),
    ]
    inlines = [AnswerInline]
    search_fields = ['question']
    list_filter = ['proj']
    list_display = ('proj','question')
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
       )


admin.site.register(Proj, ProAdmin)
admin.site.register(Ask, AskAdmin)