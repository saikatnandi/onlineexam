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

from .forms import *
from django.contrib.auth.models import User
import openpyxl
from  qa1.models import *
from readingmaterial.models import *
from django.shortcuts import render_to_response
from django.contrib import messages
from django.db.models import Q

from django.http import HttpResponseRedirect





def getString(title):
    try:
        title = str(title)
    except Exception:
        title = title.encode('UTF8')

    # print ("\n ********** retirng strign: " + title)
    return title



def get_removed_list(reading_topic, selected_topic):
    # print (type(reading_topic))
    # print (type(selected_topic))

    reading_topic_list = []
    for rt in reading_topic:
        reading_topic_list.append(rt)

    for st in selected_topic:
        for rt in reading_topic_list:
            if (rt.id == int(st)):
                # print ("*(**** about to remove")
                # print (rt)
                reading_topic_list.remove(rt)


    return reading_topic_list




@login_required(login_url="/login/")
def random_question(request):
    # reading_topic = ReadingTopic.objects.all()
    reading_topic = ReadingTopic.objects.all()
    subtopic1 = SubTopic1.objects.all()
    reading_content = ReadingContent.objects.all()

    selected_topic = []
    selected_subtopic = []
    selected_content = []
    # print ("******* requestmethod: *******: " + request.method)
    if (request.method =='POST'):
        selected_topic = request.POST.getlist('topic[]')
        selected_subtopic = request.POST.getlist('subtopic1[]')
        selected_content = request.POST.getlist('content[]')

        # print (reading_topic)
        reading_topic = get_removed_list(reading_topic, selected_topic)
        # print (reading_topic)

        # print (subtopic1)
        subtopic1 = SubTopic1.objects.filter(topic__in=reading_topic)
        # print (subtopic1)
        subtopic1 = get_removed_list(subtopic1, selected_subtopic)
        print ("\n\n ****** final subtopic")
        print (subtopic1)

        reading_content = ReadingContent.objects.filter(Q(subtopic1__in=subtopic1) | Q(reading_topic__in=reading_topic))
        reading_content = get_removed_list(reading_content, selected_content)
        print (reading_content)
        # reading_content = get_removed_list(reading_content, selected_content)


        # print (topic)
        # for t in topic:
        #     print (getString(t))
        # print ("****** topic has been printed")
        # print (subtopic)


       

        # topic2 = list([x.encode('UTF8') for x in topic])
        # print (topic2)
        # for x in t:
        #     s = getString(x)
        #     topic.append(s)

        # # topic = request.POST['topic']
        # print ("*********** topic selected")
        # print (topic)






    return render(request, 'question/random_question.html',
     {'reading_topic': reading_topic,
       'subtopic1' : subtopic1,
       'reading_content' : reading_content,
       'topic': selected_topic,
       'subtopic': selected_subtopic,
       'content' : selected_content,


     })






def index(request):
    # reading_topic = ReadingTopic.objects.all()
    question_topic = Question_Topic.objects.all()

    return render(request, 'question/index.html', {'question_topic': question_topic})


def exam_result(request, question_set_id):
    result = Question_Set_Result.objects.filter(question_set__id = question_set_id).order_by("-marks", "id")


    return render(request, 'question/exam_result.html', {'result': result})







def question_set(request, question_topic_id):
    question_set = Question_Set.objects.filter(question_topic = question_topic_id)
    return render(request, 'question/question_set.html', {'question_set': question_set})


def reading_content(request):
    # reading_topic = ReadingTopic.objects.all()
    reading_topic = ReadingTopic.objects.all()

    return render(request, 'question/reading_content.html', {'reading_topic': reading_topic})




def reading_content_topic(request, reading_topic_id):
    subtopic1 = SubTopic1.objects.filter(topic=reading_topic_id)
    # readingcontent = ReadingContent.objects.filter(subtopic1__isnull = True)
    # readingcontent = readingcontent.filter(reading_topic_id=topic_id)
    question_set = Question_Set.objects.filter(reading_topic = reading_topic_id)



    # now = timezone.now()
    # announcement = Announcement.objects.filter( Q(start_date__isnull = True) | Q(start_date__lte=now))
    # announcement = announcement.filter(Q(end_date__isnull = True) | Q(end_date__gte = now))

    return render (request, 'question/reading_content_topic.html', 
        {'subtopic1': subtopic1,
        # 'announcement' : announcement,

         'question_set': question_set,
        })





def reading_content_subtopic(request, reading_subtopic_id):
    print ("*\n\n question subtopic")
    readingcontentlist = ReadingContent.objects.filter(subtopic1=reading_subtopic_id)
    # readingcontent = ReadingContent.objects.filter(subtopic1__isnull = True)
    # readingcontent = readingcontent.filter(reading_topic_id=topic_id)
    question_set = Question_Set.objects.filter(subtopic1 = reading_subtopic_id)



    # now = timezone.now()
    # announcement = Announcement.objects.filter( Q(start_date__isnull = True) | Q(start_date__lte=now))
    # announcement = announcement.filter(Q(end_date__isnull = True) | Q(end_date__gte = now))

    return render (request, 'question/reading_content_subtopic.html', 
        {'readingcontentlist': readingcontentlist,
        # 'announcement' : announcement,

         'question_set': question_set,
        })



def reading_content_question(request, reading_content_id):
    # readingcontentlist = ReadingContent.objects.filter(subtopic1=reading_subtopic_id)
    # readingcontent = ReadingContent.objects.filter(subtopic1__isnull = True)
    # readingcontent = readingcontent.filter(reading_topic_id=topic_id)
    question_set = Question_Set.objects.filter(reading_content = reading_content_id)



    # now = timezone.now()
    # announcement = Announcement.objects.filter( Q(start_date__isnull = True) | Q(start_date__lte=now))
    # announcement = announcement.filter(Q(end_date__isnull = True) | Q(end_date__gte = now))

    return render (request, 'question/reading_content_question.html', 
        {
        # 'readingcontentlist': readingcontentlist,
        # 'announcement' : announcement,

         'question_set': question_set,
        })





def check_eligibility(request,  question_set_id):


    question_set = Question_Set.objects.filter(id = question_set_id).first()
    subscription_plan = []
    special_plan = []

    if (question_set.is_free):
        return True


    elif (not question_set.is_free):
        subscription_plan = Subscription_Plan.objects.filter(question_set= question_set)
        # special_plan = Special_Plan.objects.filter(question_set = question_set)

    
    users = Subscription.objects.filter(is_valid = True,
             subscription_plan__in=subscription_plan)
    # users = users.filter() 

    # users2 = Subscription_Special_Plan.objects.filter(is_confirmed = True)
    # users2 = users2.filter(special_plan__in=special_plan) 


    # print (users)

    for u in users:
        if (request.user == u.user):
            return True


    # for u in users2:
    #     if (request.user == u.user):
    #         return True
    # print ("\n\n******* about to rediect from check eligility")
    return False







def question_subscription(request, question_set_id):

    # print ("\n*******question set id: ")
    # print (question_set_id)
    question_set = Question_Set.objects.filter(id = question_set_id).first()
    # print (question_set)
    subscription_plan = ""
    if (not question_set.is_free):
        subscription_plan = Subscription_Plan.objects.filter(question_set = question_set)
        # special_plan = Special_Plan.objects.filter(question_set = question_set)
    




    # start_index = mcq_question.start_index() - 1


    return render(request,  'subscription/index.html', {
        'subscription': subscription_plan,  
        'question_set': question_set,
 

        })
















def question(request, question_set_id):

    ce = check_eligibility(request, question_set_id)
    if (not ce):
        url = reverse('question:question_subscription', args=(question_set_id,))
        return HttpResponseRedirect(url)
    



    mcq_question_list = Mcq_Question.objects.filter(question_set__id=question_set_id)
    question_set = Question_Set.objects.filter(id = question_set_id).first()
    if (question_set):
        total_time =  len(mcq_question_list) * question_set.individual_mcq_time
        # total_time = 5
        pass
        # question_set = question_set[0]
    else:
        print ("\n\n\n ********* this should not have printed\n this means the question_set does not exits")
        print (question_set)




    mcq_question = mcq_question_list



    question_set_result = ""
    if (request.user.is_authenticated()):

        question_set_result = Question_Set_Result.objects.filter(user= request.user,
                      question_set = question_set_id)
        if (not question_set_result):
            question_set_result = Question_Set_Result(question_set_id = question_set_id)
            question_set_result.user = request.user
        else:
            question_set_result = question_set_result[0]

        now = timezone.now()

        question_set_result.start_date = now
        question_set_result.finish_date = now + timezone.timedelta(seconds=total_time + 60)

        question_set_result.save()










    # start_index = mcq_question.start_index() - 1


    return render(request, 'question/question.html', 
        {'mcq_question':mcq_question,
         'question_set': question_set, 
          'total_time': total_time,
          # 'question_topic_id': question_topic_id, 
          'question_set_id' : question_set_id,
          'question_set_result': question_set_result,

          # 'start_index' : start_index,

          })





def result2(request, question_set_id):


    # return HttpResponse("result method")
    question_set = Question_Set.objects.filter(id = question_set_id)
    # question_set2 = Question_Set.objects.all()
    # question_set = question_set[0]
    # print (question_set)
    # print ("\n\n **** question set has been printed")
    # print (question_set2)
    return render(request, 'question/result.html',
                 {

                 # 'mcq_question':mcq_question, 
                 # 'score' : score,
                 # 'total_marks': total_marks,
                 # 'marked_mcq_str': marked_mcq_str,
                 # 'position': pos, 
                 # 'question_set': question_set,

                 }

                 )





    

def result(request, question_set_id):
    print (question_set_id)
    question_set = Question_Set.objects.filter(pk = int(question_set_id)).first()

    # print (question_set)

    if (not question_set):
        print ("*********** about to redirect")
        url = reverse('question:index')
        return HttpResponseRedirect(url)


    ce = check_eligibility(request, question_set_id)
    if (not ce):
        url = reverse('question:question_subscription', args=(question_set_id,))
        return HttpResponseRedirect(url)



        
    mcq_question_list = Mcq_Question.objects.filter(question_set__id=int(question_set_id))
     

    individual_mcq_mark = question_set.individual_mcq_marks
    negative_marking_percentage = question_set.negative_marking_percentage

    # print ("\n***** neg percenet " + str(negative_marking_percentage))

    total_marks = len(mcq_question_list) * individual_mcq_mark
    negative_marks = 0
    a = "not set"
    b = "not set"
    score = 0

    for m in mcq_question_list:
         if str(m.id) in request.POST:
            # print (m)    # print (m)

            a = request.POST[str(m.id)]
            p = checkAnswer(m, a)
            if (p == 0):
                # print ("**************worng answer")
                # print (individual_mcq_mark * negative_marking_percentage / 100)
                negative_marks += individual_mcq_mark * 1.0 * negative_marking_percentage / 100.0
            score += p * individual_mcq_mark



    marked_mcq_str = ""
    if (request.user.is_authenticated()):        
        marked_mcq = Marked_Mcq.objects.filter(user=request.user)

        marked_mcq_list = []
        for m in marked_mcq:
            marked_mcq_list.append(m.mcq_question_id)

        # print (marked_mcq_list)


    # print (marked_question)
    # print ("**********marked q str finished")
        for mcq in mcq_question_list:
            # print ("******* marked qid: " + str(mq.quick_question.id))
            if (mcq.id in marked_mcq_list):
                marked_mcq_str += str(mcq.id) + ", "
            # marked_quick_question_list.append(mq.quick_question.id)

    score = score - negative_marks



    mcq_question = mcq_question_list

    pos = ""

    if (request.user.is_authenticated()):        

        res_id = request.POST.get("result", "-1")
        if (res_id):
            res_id = int(res_id)
        else:
            res_id = -1


        # print (res_id)



        if (res_id != -1):
            question_set_result = Question_Set_Result.objects.filter(user=request.user,
             pk=res_id, question_set = question_set_id).first()

            if (question_set_result):
                now = timezone.now()

                if (now <= question_set_result.finish_date):
                    question_set_result.marks = score
                    print ("About to update marks")
                    question_set_result.save()                

                    pos = Question_Set_Result.objects.filter(question_set = question_set)
                    pos = pos.filter(marks__gt=score).count()
                    pos = pos + 1

                    print ("******* position is: ")
                    print (pos)

        else:
            pos = Question_Set_Result.objects.filter(question_set = question_set)
            pos = pos.filter(marks__gt=score).count()
            pos = pos + 1




    return render(request, 'question/result.html',
                 {'mcq_question':mcq_question, 
                 'score' : score,
                 'total_marks': total_marks,
                 'marked_mcq_str': marked_mcq_str,
                 'position': pos, 
                 'question_set': question_set,

                 }

                 )






def checkAnswer(q, ans):
    # print ("in checkAnswer method qno: %s and ans: %s\n\n" % (qno, ans))

    # print ("****in checkAnswer function: ")
    # print (q)
    # print (ans)

    # if (q.mcq_answer == "###"):
    #   answers = q.mcq_answer.split(',')

    if (q.mcq_answer == ans):
        return 1
    else:
        return 0
    






