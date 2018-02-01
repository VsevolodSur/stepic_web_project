from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def login(request, *args, **kwargs):
    return HttpResponse("It's login")