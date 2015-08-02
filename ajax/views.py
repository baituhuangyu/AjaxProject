#-*-coding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.template import RequestContext, Template, Context, loader
from django.http import HttpResponse
from models import Ajaxdb
import re
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request))

def index2(request):
    return render_to_response('index2.html',
                              context_instance=RequestContext(request))

def test(request):
    return HttpResponse("<h1>Hello world!</h1>")

def index3(request):
    items = Ajaxdb.objects.all()
    return render_to_response('index3.html',
                              {'items':items},
                              context_instance=RequestContext(request))
@csrf_exempt
def index4(request,kw=''):
    dbitems = Ajaxdb.objects.all()
    # print type(items)
    print(1)

    kw = request.GET.get('kw','default_Value')
    # kw = request.GET('kw')
    keyraw = kw
    print(keyraw)
    result=[]
    # #
    #添加输入关键字处理的代码
    #这里简单的认为输入 keyraw='快乐'，'kuaile'，'kuaine'，都处理为‘快乐’
    #  #
    # keyraw ='快乐'
    if keyraw in ['快乐','kuaile','kuaine']:
    #    key='快乐'
    # keyraw='快乐'
        key= r'.*快乐.*'.decode(encoding='utf-8')
    # print(key)
    # print(type(key))
        p=re.compile(key)
        i=0
        for string in dbitems:
            # print(2)
            # print(string.itemname)
            # print type(string.itemname)
            # print(p.findall(string.itemname))
            # print(type(p.findall(string.itemname)))
            if p.findall(string.itemname):
                # #
                # print(3)
                # 添加搜索排序算法的代码，最后选择4条最优先的Item返回
                #这里简单的筛选掉key，以数据库默认ID顺序返回。
                # #
                if string.itemname != keyraw.decode(encoding='utf-8') and i <4:
                # ##
                    result.append(string.itemname)
                    i=i+1
                # print(4)
        #以json格式返回
        obj={}
        obj={'result':result}
        relt=json.dumps(obj)
        # print(relt)
    else:
        obj={'result':''}
        relt=json.dumps(obj)

    return HttpResponse(relt)
                        # ,mimetype='application/javascript')
    # return render_to_response('index.html',
    #                           {'items': result},
    #                           context_instance=RequestContext(request))

def index5(request):
    # items = Ajaxdb.objects.all()
    return render_to_response('index5.html',
                              # {'items':items},
                              context_instance=RequestContext(request))