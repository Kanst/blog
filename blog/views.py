# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from article.models import Article
import django.shortcuts as shortcuts 
from django.views.generic import list_detail
from tagging.models import Tag, TaggedItem


def home(request):
    hello = 'Hello world!!'
    
    all_art = Article.objects.all().order_by("-add_date")
    title = ""
    return list_detail.object_list(
            request,
            queryset = Article.objects.all(),
            template_name = "index.html",
            template_object_name = "article",
            extra_context = {'title': title, 'all_art': all_art}
            )




def contact(request):
    	return render_to_response('contact.html', {'title':'Контакты - ',
                                                       })


def tags(request):
    title = "Теги |"
    return list_detail.object_list(
            request,
            queryset = Article.objects.all(),
            template_name = "tags.html",
            template_object_name = "article",
            extra_context = {'title': title,}
            )


 
