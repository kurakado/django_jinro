# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from jinro.models import Village,HN
from django.http import HttpResponse, Http404
from django.template import RequestContext
from jinro.utils import logout,login,regist

# Create your views here.
def index(request):
    village_list=Village.objects.all().order_by('id')
    free_form=None
    try:
        hn=HN.objects.get(id=request.session.get('HN'))
    except:
        hn=None
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
        else:
            free_form="登録失敗"
        


    return render_to_response('jinro/index.html',
                              {'village_list': village_list, 'HN':hn, 'free_form':free_form},context_instance=RequestContext(request))

def register(request):
    hn=request.session.get("HN")
    return render_to_response('jinro/register.html',{'HN':hn },context_instance=RequestContext(request))

def registering(request):
    hn=request.session.get("HN")
    new_HN=HN.objects.create(name=request.POST["HN"],password=request.POST["pass"])
    return index(request)
#    return render_to_response('jinro/index.html',
#            {'free_form' : "{0} is registered".format(new_HN.name)})

