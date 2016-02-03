# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from jinro.models import Village,HN
from django.http import HttpResponse, Http404
from django.template import RequestContext
from jinro.utils import logout,login

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
#    if request.POST.get("HN"):
        if login(request)==True:
#            free_form="ログイン成功"
            hn=HN.objects.get(name=request.POST.get("HN"))
#            free_form="{0} : {1}".format(free_form,hn.name)
#            free_form="{0} : {1}".format(free_form,request.session.get('HN'))
        else:
            free_form="ログイン失敗"
    #ログアウトPOST
    if request.POST.get("command")=="logout":
        logout(request)
        hn=None
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

