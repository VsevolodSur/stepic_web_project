from django.http import HttpResponse, HttpResponseNotFound
from django.template import  loader
from qa.models import Question, Answer
from django.views.decorators.http import require_GET
# from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

@require_GET
def new(request):
    questions_list = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page')
    paginator = Paginator(questions_list, limit)
    paginator.baseurl = '/?page='
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        return  HttpResponseNotFound()
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    context = {
        'questions' : questions,
        'paginator' : paginator,
    }
    template = loader.get_template('qa/question_list.html')
    return HttpResponse(template.render(context,request))

@require_GET
def popular(request):
    questions_list = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page')
    paginator = Paginator(questions_list, limit)
    paginator.baseurl = '/popular/?page='
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        return  HttpResponseNotFound()
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    context = {
        'questions' : questions,
        'paginator' : paginator,
    }
    template = loader.get_template('qa/question_list.html')
    return HttpResponse(template.render(context,request))

@require_GET
def question(request, *args, **kwargs):
    try:
        question = Question.objects.get(id=kwargs['id'])
    except:
        return  HttpResponseNotFound()
    try:
        answers = Answer.objects.filter(question=kwargs['id'])
    except Answer.DoesNotExist:
        answers = None
    context = {
        'question' : question,
        'answers' : answers,
    }
    template = loader.get_template('qa/question.html')
    return HttpResponse(template.render(context,request))

def login(request, *args, **kwargs):
    return HttpResponse("It's login")

def signup(request, *args, **kwargs):
    return HttpResponse("It's signup")

# @require_GET
# def question(request, *args, **kwargs):
#         return HttpResponse("It's question: " + kwargs['id'])

# def new(request, *args, **kwargs):
#     return HttpResponse("It's Вероника")

def ask(request, *args, **kwargs):
    return HttpResponse('ASK')
