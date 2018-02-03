from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def login(request, *args, **kwargs):
    return HttpResponse("It's login")

def signup(request, *args, **kwargs):
    return HttpResponse("It's signup")

def question(request, *args, **kwargs):
    return HttpResponse("It's question")

def popular(request, *args, **kwargs):
    return HttpResponse("It's popular")
    
def new(request, *args, **kwargs):
    return HttpResponse("It's Вероника")
   
    
    