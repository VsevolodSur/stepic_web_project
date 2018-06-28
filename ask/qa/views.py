from django.http import HttpResponse
from django.template import RequestContext, loader

def prime(request, *args, **kwargs):
    page = request.GET.get('page')
    template = loader.get_template('qa/prime.html')
    context = RequestContext(request, {
        'pagevar' : page
    })
    return HttpResponse(template.render(context))

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

def ask(request, *args, **kwargs):
    return HttpResponse('ASK')
