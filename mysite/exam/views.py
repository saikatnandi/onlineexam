from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Mcq_Question


def index(request):
    return HttpResponse("Hello, world. You're at the exam index method index.")



def show(request):
    question = Mcq_Question.objects.all()
    return render(request, 'exam/question.html', {'question': question})

def result(request):
	# if '1' in request.POST:
    a = "not set"
    b = "not set"
    if '1' in request.POST:
        a = request.POST['1']    
    b = request.POST['2']

    s = "the choices are: " + a + " and: " + b
    print ( "the choices are: " + a + " and: " + b)
    return HttpResponse(s + "<br><br>Hello, world. You're at the exam .....result method")

