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
# from .forms import Mcq_Question_Form
# from .forms import ExcelForm

# from .forms import *
from django.contrib.auth.models import User
import openpyxl
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required

import time

from django.contrib.auth import authenticate, login

from models import *
from readingmaterial.models import *
from announcement.models import *
from feedback.models import *
from subscription.models import *
from django.db.models import Q


@login_required(login_url="/login/")
def index(request):


    return render(request, 'dashboard/index.html', {
        'data': "alamin",

        })




@login_required(login_url="/login/")
def notes(request):
    # note = ContentNotes.objects.filter(user=request.user)
    reading_topic = ReadingTopic.objects.all()


    return render(request, 'dashboard/notes.html', {
        # 'note': note,
        'reading_topic' :reading_topic,
        

        })



@login_required(login_url="/login/")
def notes_topic(request, topic_id):
    reading_topic = ReadingTopic.objects.all()
    # marked_quick_question = Marked_Quick_Question.objects.filter(user = request.user).filter(
    #     quick_question__content__reading_topic_id = topic_id)
    note = ContentNotes.objects.filter(user=request.user)
    note = note.filter(Q(content__reading_topic__id = topic_id) | Q(reading_topic__id=topic_id))
    note = note.order_by("-id")
    # print (note)
    return render(request, 'dashboard/notes_topic.html', {
        'reading_topic' :reading_topic,
        'note': note,
        'topic_id': topic_id,

        })









def get_reading_topic(request, marked_mcq):
    reading_topic2 = []
    for mm in marked_mcq:
        if (mm.mcq_question.reading_topic):
            if (mm.mcq_question.reading_topic not in reading_topic2):
                reading_topic2.append(mm.mcq_question.reading_topic)

    return reading_topic2



@login_required(login_url="/login/")
def mcq_question(request):
    # reading_topic = ReadingTopic.objects.all()   
    marked_mcq = Marked_Mcq.objects.filter(user = request.user)
    reading_topic = get_reading_topic(request, marked_mcq)

    # print (reading_topic2)





    return render(request, 'dashboard/mcq_question.html', {
        'reading_topic' :reading_topic,

        })





@login_required(login_url="/login/")
def mcq_question_topic(request, topic_id):
    # reading_topic = ReadingTopic.objects.all()
    marked_mcq = Marked_Mcq.objects.filter(user = request.user)
    reading_topic = get_reading_topic(request, marked_mcq)

    marked_mcq_id = []
    for mm in marked_mcq:
        marked_mcq_id.append(mm.mcq_question_id)


    mcq_question_list = Mcq_Question.objects.filter(pk__in=marked_mcq_id)
    # print (mcq_question_list)
    if (int(topic_id) != 5555):
        # print (topic_id)
        # print (type(topic_id))
        mcq_question_list = mcq_question_list.filter(reading_topic_id = topic_id)
        # print ("******* filtering more")


    # print ("\n\n ***** going to print mcq_question_list ")
    # print (mcq_question_list)

    marked_mcq_str = ""

    for mcq in mcq_question_list:
        marked_mcq_str += str(mcq.id) + ", "



    # marked_question_str = ""
    # # print (marked_question)
    # # print ("**********marked q str finished")
    # for mq in marked_quick_question:
    #     print ("******* marked qid: " + str(mq.quick_question.id))
    #     marked_question_str += str(mq.quick_question.id) + ", "
    #     marked_quick_question_list.append(mq.quick_question.id)

    # # print (marked_quick_question_list)



    # quick_question = Quick_Question.objects.filter(pk__in = marked_quick_question_list)


    # return render(request, 'dashboard/quick_question.html', {
    #     'reading_topic' :reading_topic,
    #     'quick_question': quick_question,
    #     'marked_question_str': marked_question_str,

    #     })



    return render(request, 'dashboard/mcq_question_topic.html', {
        'reading_topic' :reading_topic,
        'mcq_question':mcq_question_list,
        'marked_mcq_str': marked_mcq_str,

        })











@login_required(login_url="/login/")
def quick_question(request):
    reading_topic = ReadingTopic.objects.all()


    return render(request, 'dashboard/quick_question.html', {
        'reading_topic' :reading_topic,

        })


@login_required(login_url="/login/")
def quick_question_topic(request, topic_id):
    reading_topic = ReadingTopic.objects.all()
    marked_quick_question = Marked_Quick_Question.objects.filter(user = request.user).filter(
        quick_question__content__reading_topic_id = topic_id)

    marked_quick_question_list = []


    marked_question_str = ""
    # print (marked_question)
    # print ("**********marked q str finished")
    for mq in marked_quick_question:
        print ("******* marked qid: " + str(mq.quick_question.id))
        marked_question_str += str(mq.quick_question.id) + ", "
        marked_quick_question_list.append(mq.quick_question.id)

    # print (marked_quick_question_list)



    quick_question = Quick_Question.objects.filter(pk__in = marked_quick_question_list)


    return render(request, 'dashboard/quick_question.html', {
        'reading_topic' :reading_topic,
        'quick_question': quick_question,
        'marked_question_str': marked_question_str,

        })








@login_required(login_url="/login/")
def notification(request):
    notification = User_Notification.objects.all().order_by('-edit_date')[:300]


    return render(request, 'dashboard/notification.html', {
        'notification': notification,

        })


@login_required(login_url="/login/")
def message(request):
    message = Message.objects.filter(user = request.user).order_by('-pub_date')[:500]


    return render(request, 'dashboard/message.html', {
        'message': message,

        })


@login_required(login_url="/login/")
def finished_content(request):
    reading_topic = ReadingTopic.objects.all()
    readingcontentlist = ReadingContent.objects.all()
    finished_content = Finished_Content.objects.filter(user=request.user)

    finished_content_str = ""

    for fc in finished_content:
        finished_content_str += str(fc.reading_content.id) + ", "

    return render(request, 'dashboard/finished_content.html', {
        'readingcontentlist': readingcontentlist,   
        'reading_topic': reading_topic, 
        'finished_content_str': finished_content_str,

        })




@login_required(login_url="/login/")
def mysubscription(request):

    # print (plan_id)

    subscription = Subscription.objects.filter(user=request.user)
    subscription = subscription.order_by('-is_valid','-is_confirmed', "-start_date","request_date")


    return render(request, 'dashboard/mysubscription.html', {
        'subscription': subscription,
 

        })




@login_required(login_url="/login/")
def myresult(request):
    print ("my result method")

    # print (plan_id)

    myresult = Question_Set_Result.objects.filter(user=request.user)
    myresult = myresult.order_by('-finish_date')

    for mr in myresult:
        pos = Question_Set_Result.objects.filter(question_set = mr.question_set)
        pos = pos.filter(marks__gt=mr.marks).count()
        print (type(pos))
        # mr.marks = 12
        mr.position = pos+1
        mr.save()

        print ("updated position ")

    # print (myresult)

    return render(request, 'dashboard/myresult.html', {
        'myresult': myresult,
 

        })
