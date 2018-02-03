from django.http import HttpResponse, Http404 

def myroot(request, *args, **kwargs):
    return HttpResponse("It's root!")

def ask(request, *args, **kwargs):
    return HttpResponse("It's ask!")

def err404(request, *args, **kwargs):
    raise Http404(request)
