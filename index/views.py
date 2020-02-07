import functools

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from index.models import RankingList


def login_required(func):
    @functools.wraps(func)  # 修饰内层函数，防止当前装饰器去修改被装饰函数__name__的属性
    def inner(request, *args, **kwargs):
        user = request.session.get('cname', None)
        print(user)
        if not user:
            return redirect('/login/')
        else:
            return func(request, *args, **kwargs)

    return inner


@login_required
def createClient(request):
    if request.method == 'GET':
        return render(request, 'createClient.html')
    if request.method == 'POST':
        cname = request.POST.get('cname', 0)
        if cname:
            try:
                RankingList.objects.get(cname=cname)
                return HttpResponse('客户端已存在')
            except:
                RankingList.objects.create(cname=cname, cscore=0)
                request.session['cname'] = cname
                return redirect('/index/')
        else:
            return HttpResponse('客户端名不能为空')


@login_required
def setScore(request):
    if request.method == 'GET':
        return render(request, 'setScore.html')

    if request.method == 'POST':
        cname = request.session.get('cname', None)
        cscore = request.POST.get('cscore', 0)
        try:
            cscore = int(cscore)
        except:
            return HttpResponse('请输入一个0到10000000之间的数值')
        if 0 <= cscore <= 10000000 and cname:
            try:
                info = RankingList.objects.get(cname=cname)
                info.cscore = cscore
                info.save()
                return HttpResponse('修改成功')
            except:
                return HttpResponse('该客户端不存在')
        else:
            return HttpResponse('请输入正确的分数')
    return HttpResponse('请求方式错误')


@login_required
def getRankList(request):
    if request.method == 'GET':
        cname = request.session['cname']
        pageNum = request.GET.get("pageNum", 1)
        allClient = RankingList.objects.all().order_by('-cscore')
        pageinator = Paginator(allClient, 10)
        try:
            pageNum = int(pageNum)
        except:
            return HttpResponse('页码不存在')
        try:
            info = RankingList.objects.get(cname=cname)
        except:
            return HttpResponse("该客户端不存在")

        currentRank = RankingList.objects.filter(cscore__gt=info.cscore).count() + 1

        if pageNum > pageinator.num_pages:
            pageNum = pageinator.num_pages
        elif pageNum < 1:
            pageNum = 1
        rankList = pageinator.page(pageNum)
        perLoc = 10 * (pageNum - 1)
        for rank in rankList:
            perLoc += 1
            rank.location = perLoc

        return render(request, 'getRank.html', {'info': info, 'currentRank': currentRank, 'rankList': rankList})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    cname = request.POST.get('cname', None)
    if not cname:
        return HttpResponse('请输入客户端名称')
    try:
        RankingList.objects.get(cname=cname)
        request.session['cname'] = cname
        return redirect('/index/')
    except:
        return HttpResponse('该客户端不存在')


def index(request):
    return render(request, 'index.html')


def logout(request):
    request.session.flush()
    return HttpResponse('退出登录')
