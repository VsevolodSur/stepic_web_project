from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import  loader
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import get_object_or_404, render
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
        # return  HttpResponseNotFound()
        # return  HttpResponse("PageNotAnInteger")
        questions = paginator.page(1)
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
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    context = {
        'questions' : questions,
        'paginator' : paginator,
    }
    template = loader.get_template('qa/question_list.html')
    return HttpResponse(template.render(context,request))

def question(request, *args, **kwargs):
    try:
        question = Question.objects.get(id=kwargs['id'])
    except:
        return  HttpResponseNotFound()
    try:
        answers = Answer.objects.filter(question=kwargs['id'])
    except Answer.DoesNotExist:
        answers = None
    form = AnswerForm(question.text)
    context = {
        'question' : question,
        'answers' : answers,
        'form': form,
    }
    template = loader.get_template('qa/question.html')
    return HttpResponse(template.render(context,request))

def login(request, *args, **kwargs):
    return HttpResponse("It's login")

def signup(request, *args, **kwargs):
    return HttpResponse("It's signup")

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    context = {
        'form': form,
    }
    template = loader.get_template('qa/ask_form.html')
    return HttpResponse(template.render(context,request))
    # return render(request, 'qa/ask_form.html', {'form': form,})

def answer(request, *args, **kwargs):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = answer.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    context = {
        'form': form,
    }
    template = loader.get_template('qa/answer_form.html')
    return HttpResponse(template.render(context,request))
