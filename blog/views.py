# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from article.models import Article
import django.shortcuts as shortcuts 
from django.views.generic import list_detail
from tagging.models import Tag, TaggedItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def pagination_sokr(request,page):
    books_list = request
    paginator = Paginator(books_list, 5)
    try:
        request = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        request = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        request = paginator.page(paginator.num_pages)
    return request

def home(request):
    hello = 'Hello world!!'
    
    all_art = pagination_sokr(Article.objects.all().order_by("-add_date"), request.GET.get('page'))
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


 
