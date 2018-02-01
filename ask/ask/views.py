from django.http import HttpResponse 

def myroot(request, *args, **kwargs):
    return HttpResponse("It's root!")

def ask(request, *args, **kwargs):
    return HttpResponse("It's ask!")
