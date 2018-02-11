from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def login(request, *args, **kwargs):
    return HttpResponse("It's login")

def signup(request, *args, **kwargs):
    return HttpResponse("It's signup")

# def question(request, *args):
# return HttpResponse("It's question: " + args[0])
def question(request, *args, **kwargs):
        return HttpResponse("It's question: " + kwargs['id'])

def popular(request, *args, **kwargs):
    return HttpResponse("It's popular")
    
def new(request, *args, **kwargs):
    return HttpResponse("It's Вероника")
   
    
    