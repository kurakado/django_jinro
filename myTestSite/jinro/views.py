# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from jinro.models import Village,HN
from django.http import HttpResponse, Http404
from django.template import RequestContext
from jinro.utils import logout,login,regist,getHN_fromSession

# Create your views here.
def index(request):
    village_list=Village.objects.all().order_by('id')
    free_form=None
    hn=getHN_fromSession(request)
    #ログインPOST
    if request.POST.get("command")=="login":
        if login(request)==True:
            hn=HN.objects.get(name=request.POST.get("HN"))
        else:
            free_form="ログイン失敗"
    #ログアウトPOST
    elif request.POST.get("command")=="logout":
        logout(request)
        hn=None
    #登録POST
    elif request.POST.get("command")=="regist":
        input_name=request.POST.get("HN")
        input_pass=request.POST.get("pass")
        if regist(input_name,input_pass)==True:
            free_form="登録成功"
            hn=HN.objects.get(name=input_name)
            request.session['HN'] = hn.id
        else:
            free_form="登録失敗"
        


    return render_to_response('jinro/index.html',
                              {'village_list': village_list, 'HN':hn, 'free_form':free_form},context_instance=RequestContext(request))

def register(request):
    hn=getHN_fromSession(request)
    return render_to_response('jinro/register.html',{'HN':hn },context_instance=RequestContext(request))

def makeVillage(request):
    hn=getHN_fromSession(request)
    return render_to_response('jinro/makeVillage.html',{'HN':hn },context_instance=RequestContext(request))

def joinVillage(request):
    hn=getHN_fromSession(request)
    village_list=Village.objects.all().order_by('id')
    return render_to_response('jinro/joinVillage.html',{'HN':hn,'village_list':village_list},context_instance=RequestContext(request))

def game(request,village_number):
    hn=getHN_fromSession(request)
    try:
        village=Village.objects.get(village_number)
        #
    except:
        free_form="該当の村が存在しません"
        return render_to_response('jinro/index.html',
                              {'HN':hn, 'free_form':free_form},context_instance=RequestContext(request))
    return ender_to_response('jinro/game.html',{'HN':hn},context_instance=RequestContext(request))
