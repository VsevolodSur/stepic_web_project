#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404 

def myroot(request, *args, **kwargs):
    return HttpResponse("It's root!")

def ask(request, *args, **kwargs):
    return HttpResponse("It's ask!")

def err404(request, *args, **kwargs):
    raise Http404()
    # return HttpResponse(
    #     content = "<html><head><meta charset='utf-8'>Ничего такого нет...</head></html>",
    #     content_type = "text/html",
    #     status = 404,)

