# -*- coding: utf-8 -*-
from django.contrib import admin
from askq.models import Proj, Ask, Answer

class AskInline(admin.TabularInline):
    model = Ask
    extra = 0
    fieldsets = [
        ( 'Вопрос', {'fields': ['question'], 'classes': ['wide']}),
    ]

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0
    fieldsets = [
        ( None, {'fields': ['ans'], 'classes': ['wide']}),
    ]

class ProAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Имя поекта', {'fields': ['projectname'], 'classes': ['wide']}),
        ('Адрес проекта', {'fields': ['urlp']}),
    ]
    inlines = [AskInline]
    list_display = ('projectname', 'urlp')

class AskAdmin(admin.ModelAdmin):
    ordering = ('proj',)
#    readonly_fields = ('proj',)
    fieldsets = [
        ('Проект', {'fields':['proj']}),
        ('Вопрос', {'fields': ['question']}),
    ]
    inlines = [AnswerInline]
    list_display = ('proj','question')
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )


admin.site.register(Proj, ProAdmin)
admin.site.register(Ask, AskAdmin)