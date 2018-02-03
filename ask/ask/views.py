from django.http import HttpResponse 

def myroot(request, *args, **kwargs):
    return HttpResponse("It's root!")

def ask(request, *args, **kwargs):
    return HttpResponse("It's ask!")

def err404(request, *args, **kwargs):
    return HttpResponse("404")
