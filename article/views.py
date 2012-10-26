# Create your views here.
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
    a = request.path
    a = str(a).split("/")[2]
    idi = a.split("-")

    art = Article.objects.get(id=idi[0])
    tegi = str(art.tags).split(",")
    title = ""
    return list_detail.object_list(
            request,
            queryset = Article.objects.all(),
            template_name = "article/index.html",
            template_object_name = "article",
            extra_context = {'title': title, 'art': art,'tegi':tegi}
            )



 
def with_tag(request, tag, object_id=None): 
    title = tag + " |"
    all_art = Article.objects.filter(tags__contains=tag)
    
    return list_detail.object_list(
            request,
            queryset = Article.objects.all(),
            template_name = "article/art_in_tags.html",
            template_object_name = "article",
            extra_context = {'title': title, 'all_art':all_art}
            )


