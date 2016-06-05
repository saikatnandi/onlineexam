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

from django.contrib.auth.models import User

from qa1.models import MarkedText
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *
from django.shortcuts import render_to_response
from django.contrib import messages
# from django.core.context_processors import csrf

from  django.template.context_processors import csrf

from announcement.models import *
from django.db.models import Q
from qa1.models import *
import json

def getString(title):
    try:
        title = str(title)
    except Exception:
        title = title.encode('UTF8')

    # print ("\n ********** retirng strign: " + title)
    return title


def getContentMarkedMcqString(content_marked_mcq):
    cmm = ""
    for m in content_marked_mcq:
        if (m.mcq_question is not None):
            cmm += str(m.mcq_question.id) + ', '  

    return cmm 


def quick_question_details(request, quick_question_id):
    quick_question = Quick_Question.objects.filter(id=quick_question_id)

    return render(request, 'readingmaterial/quick_question_details.html',
        {
        'quick_question': quick_question,             

        })



def mcq_question_details(request, mcq_question_id):
    mcq_question = Mcq_Question.objects.filter(id=mcq_question_id)

    return render(request, 'readingmaterial/mcq_question_details.html',
        {
        'mcq_question': mcq_question,             

        })



def index(request):
    reading_topic = ReadingTopic.objects.all()

    now = timezone.now()
    announcement = Announcement.objects.filter( Q(start_date__isnull = True) | Q(start_date__lte=now))
    announcement = announcement.filter(Q(end_date__isnull = True) | Q(end_date__gte = now))


    return render(request, 'readingmaterial/index.html',
        {'reading_topic': reading_topic,
        'announcement' : announcement,        

        })

def subtopic1(request, topic_id):
    reading_topic = ReadingTopic.objects.all()
    subtopic1 = SubTopic1.objects.filter(topic=topic_id)
    readingcontent = ReadingContent.objects.filter(subtopic1__isnull = True)
    readingcontent = readingcontent.filter(reading_topic_id=topic_id)
    current_topic = ReadingTopic.objects.filter(id=topic_id).first()


    # mcq_question = Mcq_Question.objects.filter(reading_topic__id=topic_id)


    now = timezone.now()
    announcement = Announcement.objects.filter( Q(start_date__isnull = True) | Q(start_date__lte=now))
    announcement = announcement.filter(Q(end_date__isnull = True) | Q(end_date__gte = now))

    return render (request, 'readingmaterial/subtopic1.html', 
        {'subtopic1': subtopic1,
        'announcement' : announcement,
        'readingcontent' : readingcontent,
         'topic_id' : topic_id,
         'reading_topic': reading_topic,
         'current_topic': current_topic,
         # 'mcq_question':mcq_question,


        })

def subtopic1_mcq(request, topic_id, choice):
    # print ("subtopic mcq method")
    # print ("choice: " + choice)
    # reading_topic = ReadingTopic.objects.all()
    # subtopic1 = SubTopic1.objects.filter(topic=topic_id)
    # readingcontent = ReadingContent.objects.filter(subtopic1__isnull = True)
    # readingcontent = readingcontent.filter(reading_topic_id=topic_id)
    # current_topic = ReadingTopic.objects.filter(id=topic_id).first()

    mcq_question = ""
    if (int(choice) == 1):
        mcq_question = Mcq_Question.objects.filter(reading_topic__id=topic_id)
        print ("in if condition ")
    elif (int(choice) == 2):
        mcq_question = Mcq_Question.objects.filter(reading_topic__id=topic_id)
        mcq_question = mcq_question.filter(Q(subtopic1__isnull=False) | Q(reading_content__isnull=False))
    elif (int(choice) == 3):
        mcq_question = Mcq_Question.objects.filter(reading_topic__id=topic_id)
        mcq_question = mcq_question.filter(subtopic1__isnull=True, reading_content__isnull=True)

    marked_mcq_str = ""
    if (request.user.is_authenticated()):        
        marked_mcq = Marked_Mcq.objects.filter(user=request.user)
        marked_mcq_str = getContentMarkedMcqString(marked_mcq)


    # print (mcq_question)

    now = timezone.now()
    announcement = Announcement.objects.filter( Q(start_date__isnull = True) | Q(start_date__lte=now))
    announcement = announcement.filter(Q(end_date__isnull = True) | Q(end_date__gte = now))

    return render ( request, 'question/result.html',  
        {
        # 'subtopic1': subtopic1,
        # 'announcement' : announcement,
        # 'readingcontent' : readingcontent,
        #  'topic_id' : topic_id,
        #  'reading_topic': reading_topic,
        #  'current_topic': current_topic,
        'is_exam': '0',
        'mcq_question':mcq_question, 
        'marked_mcq_str': marked_mcq_str,


        })




def reading_content_list(request, subtopic1_id):
    reading_topic = ReadingTopic.objects.all()
    readingcontentlist = ReadingContent.objects.filter(subtopic1=subtopic1_id)

    current_sub_topic = SubTopic1.objects.filter(id=subtopic1_id).first()

    now = timezone.now()
    announcement = Announcement.objects.filter( Q(start_date__isnull = True) | Q(start_date__lte=now))
    announcement = announcement.filter(Q(end_date__isnull = True) | Q(end_date__gte = now))

    return render (request, 'readingmaterial/readingcontentlist.html', 
        {'readingcontentlist': readingcontentlist,
        'announcement' : announcement,
        'reading_topic': reading_topic,
        'current_sub_topic': current_sub_topic,
        


        })
    #return HttpResponse("Hello, world. You're at the .... reading material ..... index.")


def reading_content_list_mcq(request, subtopic1_id, choice):
    reading_topic = ReadingTopic.objects.all()
    readingcontentlist = ReadingContent.objects.filter(subtopic1=subtopic1_id)

    current_sub_topic = SubTopic1.objects.filter(id=subtopic1_id).first()

    mcq_question = ""
    if (int(choice) == 1):
        mcq_question = Mcq_Question.objects.filter(subtopic1__id=subtopic1_id)
        # print ("in if condition ")
    elif (int(choice) == 2):
        mcq_question = Mcq_Question.objects.filter(subtopic1__id=subtopic1_id)
        mcq_question = mcq_question.filter(reading_content__isnull=False)
    elif (int(choice) == 3):
        mcq_question = Mcq_Question.objects.filter(subtopic1__id=subtopic1_id)
        mcq_question = mcq_question.filter(reading_content__isnull=True)

    marked_mcq_str = ""

    if (request.user.is_authenticated()):        
        marked_mcq = Marked_Mcq.objects.filter(user=request.user)
        marked_mcq_str = getContentMarkedMcqString(marked_mcq)





    now = timezone.now()
    announcement = Announcement.objects.filter( Q(start_date__isnull = True) | Q(start_date__lte=now))
    announcement = announcement.filter(Q(end_date__isnull = True) | Q(end_date__gte = now))

    return render (request, 'question/result.html', 
        {'readingcontentlist': readingcontentlist,
        'announcement' : announcement,
        'reading_topic': reading_topic,
        'current_sub_topic': current_sub_topic,
        'is_exam': '0',
        'mcq_question':mcq_question, 
        'marked_mcq_str': marked_mcq_str,

        


        })










def reading_content_details(request, reading_content_id):
    reading_topic = ReadingTopic.objects.all()
    readingcontent = ReadingContent.objects.get(id=reading_content_id)
    quick_question = Quick_Question.objects.filter(content = reading_content_id)

    readingcontent_text = ""
    content_marked_mcq = ""

    if (request.user.is_authenticated()):
        # print ("*********authenticated user*********")
        readingcontent_text = ContentMarkedText.objects.filter(user = request.user,
         content_id = reading_content_id)
    
        # content_marked_mcq = ContentMarkedMcq.objects.filter( user=request.user)

    # readingcontentlist = ReadingContent.objects.filter(subtopic1=subtopic1_id)


    comment = ContentComment.objects.filter(content = readingcontent).order_by("-pub_date")


    # print ("\n cmm is: %s" % cmm)
    note = None
    marked_question_str = ""
    finished = ""
    if (request.user.is_authenticated()):
        cmm = getContentMarkedMcqString(content_marked_mcq)
        note = ContentNotes.objects.filter(user=request.user, content=reading_content_id)
        note = note.order_by("-id")

        marked_question = Marked_Quick_Question.objects.filter(user=request.user)


        # print (marked_question)
        # print ("**********marked q str finished")
        for mq in marked_question:

            if (str(mq.quick_question.content_id) == str(reading_content_id)):
                marked_question_str += str(mq.quick_question.id) + ", "

        finished = Finished_Content.objects.filter(user=request.user, reading_content_id = reading_content_id)
        print (finished)

        if (finished):
            finished = True
        else:
            finished = False


    # print ("*****going to return template\n")
    # print (marked_question_str)
    # print ("**********marked q str finished")
    now = timezone.now()
    announcement = Announcement.objects.filter( Q(start_date__isnull = True) | Q(start_date__lte=now))
    announcement = announcement.filter(Q(end_date__isnull = True) | Q(end_date__gte = now))

    question_set = Question_Set.objects.filter(reading_content = readingcontent)

    print (question_set)

    return render (request, 'readingmaterial/reading_content_details.html', 
        {'readingcontent': readingcontent, 
         'quick_question' : quick_question,
         # 'topic_id' : topic_id,
        # 'readingcontentlist': readingcontentlist,
        'reading_content_id': reading_content_id,
        'note': note, 
        'comment': comment,
        'finished': finished,
        # 'mcq_question': mcq_question, 
        # 'content_marked_mcq_string': cmm,
        'marked_question_str': marked_question_str,
        'readingcontent_text': readingcontent_text,
        'announcement' : announcement,
        'reading_topic': reading_topic,
        'question_set': question_set,

        })
    #return HttpResponse("Hello, world. You're at the .... reading material ..... index.")




def reading_content_details_mcq(request, reading_content_id):


    mcq_question = Mcq_Question.objects.filter(reading_content__id=reading_content_id)
    marked_mcq_str = ""

    if (request.user.is_authenticated()):        
        marked_mcq = Marked_Mcq.objects.filter(user=request.user)
        marked_mcq_str = getContentMarkedMcqString(marked_mcq)





    now = timezone.now()
    announcement = Announcement.objects.filter( Q(start_date__isnull = True) | Q(start_date__lte=now))
    announcement = announcement.filter(Q(end_date__isnull = True) | Q(end_date__gte = now))

    return render (request, 'question/result.html', 
        {


        'announcement' : announcement,
        # 'reading_topic': reading_topic,
        # 'current_sub_topic': current_sub_topic,
        'is_exam': '0',
        'mcq_question':mcq_question, 
        'marked_mcq_str': marked_mcq_str,

        


        })











def reading_content_finished(request, reading_content_id):

    print ("*&********* going to do something now")
    try:        
        fc = Finished_Content(user=request.user)
        fc.reading_content_id = reading_content_id
        fc.save()
    except Exception:
        print ("\n ****** there is an exception")
        


    return HttpResponseRedirect(reverse('readingmaterial:content', args=[reading_content_id]))





def reading_content_unfinished(request, reading_content_id):

    finished = Finished_Content.objects.get(user=request.user, reading_content_id = reading_content_id)
    if (finished):
        finished.delete()

    return HttpResponseRedirect(reverse('readingmaterial:content', args=[reading_content_id]))




def varification(request):
    return render(request, 'readingmaterial/include/google6bac80d6112145d3.html')










from .views_ajax import *