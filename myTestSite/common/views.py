# -*- coding: utf-8 -*-
#
from django.shortcuts import render_to_response, get_object_or_404
#from django.template import Context, loader
from django.http import HttpResponse, Http404
from django.template import RequestContext

def index(request):
    return render_to_response('index.html')
