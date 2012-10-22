# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def home(request):
    hello = 'Hello world!!'
    return render_to_response('index.html', {'hello':hello}, context_instance=RequestContext(request))

def contact(request):
	return render_to_response('contact.html', {'title':'Библиотека Kanst9',
                                                   })


