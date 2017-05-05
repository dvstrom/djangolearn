from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    # return HttpResponse("Hello, world, you're at the polls index!")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = '.  '.join([p.question_text for p in latest_question_list])
    # return HttpResponse(output)
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're are voting on question %s" % question_id)
