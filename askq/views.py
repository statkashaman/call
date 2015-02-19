# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, Count
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from askq.models import Proj, Ask, Answer, Stats
from askq.forms import ProjForm
import datetime
import xlwt


def translit(locallangstring):
    conversion = {
        u'\u0410': 'A', u'\u0430': 'a',
        u'\u0411': 'B', u'\u0431': 'b',
        u'\u0412': 'V', u'\u0432': 'v',
        u'\u0413': 'G', u'\u0433': 'g',
        u'\u0414': 'D', u'\u0434': 'd',
        u'\u0415': 'E', u'\u0435': 'e',
        u'\u0401': 'Yo', u'\u0451': 'yo',
        u'\u0416': 'Zh', u'\u0436': 'zh',
        u'\u0417': 'Z', u'\u0437': 'z',
        u'\u0418': 'I', u'\u0438': 'i',
        u'\u0419': 'Y', u'\u0439': 'y',
        u'\u041a': 'K', u'\u043a': 'k',
        u'\u041b': 'L', u'\u043b': 'l',
        u'\u041c': 'M', u'\u043c': 'm',
        u'\u041d': 'N', u'\u043d': 'n',
        u'\u041e': 'O', u'\u043e': 'o',
        u'\u041f': 'P', u'\u043f': 'p',
        u'\u0420': 'R', u'\u0440': 'r',
        u'\u0421': 'S', u'\u0441': 's',
        u'\u0422': 'T', u'\u0442': 't',
        u'\u0423': 'U', u'\u0443': 'u',
        u'\u0424': 'F', u'\u0444': 'f',
        u'\u0425': 'H', u'\u0445': 'h',
        u'\u0426': 'Ts', u'\u0446': 'ts',
        u'\u0427': 'Ch', u'\u0447': 'ch',
        u'\u0428': 'Sh', u'\u0448': 'sh',
        u'\u0429': 'Sch', u'\u0449': 'sch',
        u'\u042a': '"', u'\u044a': '"',
        u'\u042b': 'Y', u'\u044b': 'y',
        u'\u042c': '\'', u'\u044c': '\'',
        u'\u042d': 'E', u'\u044d': 'e',
        u'\u042e': 'Yu', u'\u044e': 'yu',
        u'\u042f': 'Ya', u'\u044f': 'ya',
        u'\u0020': '_'
    }
    translitstring = []
    for c in locallangstring:
        translitstring.append(conversion.setdefault(c, c))
    return ''.join(translitstring)


def forma(a):
    form = ProjForm()
    form.fields["projectname"].initial = a
    return form


def poisk(a, *args):
    lq = a.split()
    qs = Q()
    for i in lq:
        qs.add(Q(["question__icontains", i]), 'AND')
    if args:
        sq = Ask.objects.filter(qs).filter(proj=args)
    else:
        sq = Ask.objects.filter(qs)
    return sq


def current_project(a):
    cur_proj = Proj.objects.get(id=a)
    return cur_proj


def voprosi(*args):
    askp = Ask.objects.filter(proj=args)
    return askp


def current_vopros(a):
    cur_ask = Ask.objects.get(id=a)
    return cur_ask


def otvet(*args):
    try:
        answers = Answer.objects.filter(ask_id=args)
    except ObjectDoesNotExist:
        answers = "К сожалению пока нету ответа"
    return answers


def stats(a, b):
    date_now = datetime.date.today()
    da = Stats(proj_id=a, ask_id=b, date_ask=date_now)
    da.save()


def stats_select(a, b, c):
    ss = Stats.objects.filter(proj_id=a).exclude(date_ask__gte=c).filter(date_ask__gte=b).values("ask_id").annotate(
        num_ask=Count("ask_id")).order_by("-num_ask")
    return ss


def xls_to_response(xls, fname):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = "attachment; filename = %s" % fname
    xls.save(response)
    return response


def index(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if 'projectname' in request.GET:
            prname = request.GET['projectname']
            if 'cur_ask' in request.GET:
                cur_ask = request.GET['cur_ask']
                stats(prname, cur_ask)
                context = {'form': forma(prname), 'sq': poisk(q, prname), 'query': q,
                           'cur_proj': current_project(prname), 'cur_ask': current_vopros(cur_ask),
                           'answer': otvet(cur_ask)}
            else:
                context = {'form': forma(prname), 'sq': poisk(q, prname), 'query': q,
                           'cur_proj': current_project(prname)}
        else:
            if 'cur_ask' in request.GET:
                prname = request.GET['project']
                cur_ask = request.GET['cur_ask']
                stats(prname, cur_ask)
                context = {'form': forma(prname), 'sq': poisk(q), 'query': q, 'cur_ask': current_vopros(cur_ask),
                           'answer': otvet(cur_ask), 'cur_search_proj': current_project(prname)}
            else:
                context = {'form': forma(0), 'sq': poisk(q), 'query': q}
    else:
        if 'projectname' in request.GET:
            if request.GET['projectname'] == '':
                return HttpResponseRedirect("/call/")
            else:
                prname = request.GET['projectname']
                if 'cur_ask' in request.GET:
                    cur_ask = request.GET['cur_ask']
                    stats(prname, cur_ask)
                    context = {'form': forma(prname), 'askp': voprosi(prname), 'cur_proj': current_project(prname),
                               'answer': otvet(cur_ask), 'cur_ask': current_vopros(cur_ask)}
                else:
                    context = {'form': forma(prname), 'askp': voprosi(prname), 'cur_proj': current_project(prname)}
        else:
            context = {'form': forma(0)}
    return render(request, 'askq/index.html', context)


def statistics(request):
    if 'projectname' in request.GET:
        if request.GET['projectname'] == '':
            return HttpResponseRedirect("/call/stat/")
        elif 'date_ot' and 'date_do' in request.GET:
            prname = request.GET['projectname']
            if request.GET['date_ot'] == '':
                context = {'form': forma(prname), 'check_date': 1}
            elif request.GET['date_do'] == '':
                context = {'form': forma(prname), 'check_date': 1}
            else:
                prname = request.GET['projectname']
                date_ot = request.GET['date_ot']
                date_do = request.GET['date_do']
                context = {'form': forma(prname), 'result': stats_select(prname, date_ot, date_do),
                           'askp': voprosi(prname), 'cur_proj': current_project(prname), 'date_ot': date_ot,
                           'date_do': date_do}

    else:
        context = {'form': forma(0)}
    return render(request, 'askq/statistics.html', context)


def excel_output(request):
    if request.GET['projectname'] == '':
        return HttpResponseRedirect("/call/stat/")
    book = xlwt.Workbook(encoding='utf8')
    ws0 = book.add_sheet('List 1')
    prname = request.GET['projectname']
    date_ot = request.GET['date_ot']
    date_do = request.GET['date_do']
    results = stats_select(prname, date_ot, date_do)
    askps = voprosi(prname)
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style = xlwt.XFStyle()
    style.alignment = alignment
    ws0.write_merge(0, 0, 0, 1, u'Cтатиcтика по проекту:  ' + current_project(
        prname).projectname + u'  с  ' + date_ot + u'  по  ' + date_do, style)
    ws0.col(0).width = 80 * 256
    st = 1
    for askp in askps:
        for result in results:
            if result['ask_id'] == askp.id:
                ws0.write(st, 0, askp.question)
                ws0.write(st, 1, result['num_ask'])
                st += 1
    return xls_to_response(book,
                           translit(current_project(prname).projectname) + "_" + str(datetime.date.today()) + ".xls")

