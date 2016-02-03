# -*- coding: utf-8 -*-
from django.http import HttpResponse
from jinro.models import Village,HN

def login(request):
    hn=HN.objects.filter(name=request.POST.get('HN'))
    if len(hn)==0:
        return False
    hn=hn[0]
    if hn.password==request.POST['pass']:
        request.session['HN'] = hn.id
        return True
    return False

def logout(request):
    try:
        del request.session['HN']
        return True
    except KeyError:
        return False
