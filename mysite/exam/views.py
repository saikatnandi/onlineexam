from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Mcq_Question
from .models import Topic
from .models import Question_Set



def index(request):
    return HttpResponse("Hello, world. You're at the exam index method index.")

def startexam(request, question_set_id):
    question = Mcq_Question.objects.filter(question_set = question_set_id)
    return render(request, 'exam/question.html', {'question': question})


def home(request):
    topic = Topic.objects.all()

    question_set = []

    for t in topic:
        qs = Question_Set.objects.filter(topic = t.id)
        question_set.append(qs)
        print (qs)
        print()
    print (question_set)
    return render(request, 'exam/home.html', {'topic': topic, 'question_set': question_set})


def show(request):
    question = Mcq_Question.objects.all()
    return render(request, 'exam/question.html', {'question': question})

def result(request):
	# if '1' in request.POST:
    question = Mcq_Question.objects.all()
    print("from result")
    print (question)
    print (question[0])

    a = "not set"
    b = "not set"
    score = 0

    for q in question:
    	
	    if str(q.id) in request.POST:
	        a = request.POST[str(q.id)]  

	        p = checkAnswer(question, q.id, a)
	        score += p
	        print ("............%s...%d" % (str(q), p)) 

    # if '2' in request.POST: 
    #     b = request.POST['2']

    s = "the choices are: " 
    
    print ( "the choices are: " + a + " and: ")
    # return HttpResponse(s + "<br><br>Hello, world. You're at the exam .....result method score is %d<br> " % score)
    return render(request, 'exam/result.html', {'score': score})








def checkAnswer(question, qno, ans):
	# print ("in checkAnswer method qno: %s and ans: %s\n\n" % (qno, ans))
	for q in question:
		if (q.id == qno):
			if (q.mcq_answer == ans):
				return 1
			else:
				return 0
	return 0











