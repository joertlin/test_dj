#from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {'latest_question_list': latest_question_list})
	return HttpResponse(template.render(context))
	#output = ', '.join([p.question_text for p in latest_question_list])
	#return HttpResponse(output)
	#return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response =  "Your're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on questions %s." % question_id)

# Create your views here.
