from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from .forms import NameForm
from .forms import Mcq_Question_Form
from .forms import UploadFileForm
from django.contrib.auth.models import User

from .models import Mcq_Question
from .models import Topic
from .models import Question_Set
from qa1.models import MarkedText
# from mcq.models import MarkedText
from django.views.decorators.csrf import csrf_exempt


from django.contrib import auth                 
# from django.core.context_processors import csrf 
# from forms import MyRegistrationForm
from  django.template.context_processors import csrf






def index(request):
    st = ""
    if not request.user.is_authenticated():
        st += "noooooooooooooooooooooooooooooot authenticated<br><br>"
    else:
        st += "authenticated..................................user name: " + request.user.username + "<br><br>"
        st += "and user id is:" + str(request.user.id) + " <br>"
        st += "last name is: " + str(request.user.last_name) + "<br>"


    st += "<br>Hello, world. You're at the exam index method index."
    return HttpResponse(st  )

@login_required(login_url="/login/")
def ajax(request):

    print ("\n\n in ajax function \n\n")

    if request.method == 'POST':
        text = request.POST.get('text2', 'No data has been sent')
        aj = MarkedText(marked_text=text)
        aj.user = request.user
        aj.save()

        return HttpResponse("ajax successful sent from the dajngo ajax function")
    

    return render(request, 'exam/ajax.html')




def startexam(request, question_set_id):
    question = Mcq_Question.objects.filter(question_set = question_set_id)
    return render(request, 'exam/question.html', {'question': question})

# def logout(request):
#     print ("\n\ngoint to logout the user")
#     django_logout(request)
#     return redirect('/exam/')

def testform(request):
    form = Mcq_Question_Form()
    return render(request, 'exam/name.html', {'form': form})




def fileupload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print ("\n this is a post method \n")
        if form.is_valid():
            print ("the form is valid\n")
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/exam/')
    else:
        print ('\nthe form is not valid so returning\n')
        form = UploadFileForm()
    
    return render(request, 'exam/fileupload.html', {'form': form})





def handle_uploaded_file(f):
    print ("handing uploaded files")














def myregistration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            username = ""
            password = ""
            email = ""
            res = ""
            if 'username' in request.POST:
                res += "Your name is: " + request.POST['username']
                username = request.POST['username']
            if 'password' in request.POST:
                
                password = request.POST['password']
                res += " password is: " + password
            if 'email' in request.POST:

                email = request.POST['email']
                res += " email is: " + email
                
    


            if username and password and email:
                print("\ngoing to create account\n")

                if User.objects.filter(username=username).exists():
                    res += "<br>........<br><br> username: " + username + " already exists"
                else:
                    user = User.objects.create_user(username, email, password)
                    res += "<br> .........account has been created successfully <br>"




            return HttpResponse(res)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'exam/myregistration.html', {'form': form,'alamin':'This is a dummy variable created by alamin'})








@login_required(login_url="/exam/login/")
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











