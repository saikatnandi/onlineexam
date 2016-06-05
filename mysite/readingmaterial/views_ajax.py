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
from feedback.models import *
from django.db.models import Q
from qa1.models import *
import json


# from . import views_0







def ajax_addnote(request):
    # print ("\n............addnote ajax is called....\n")
    if (request.method =='POST'):
        note = request.POST.get('note', 'no comment')
        #userId = request.POST.get('userId', 'no user id')
        reading_content_id = request.POST.get('reading_content_id', '')
        reading_topic_id = request.POST.get('reading_topic_id', '')





        #print ("post id is: ..........." + postId)
        # print (note)
        # print (reading_content_id)

        mynote = getString(note)
        c = ContentNotes(content_notes=mynote)

        c.user = request.user



        if (reading_content_id):
            
            con = ReadingContent.objects.get(id=int(reading_content_id))
            c.content = con
        elif (reading_topic_id):
            print ("******** In else if condition notes with topic id")
            topic = ReadingTopic.objects.get(id=int(reading_topic_id))
            c.reading_topic = topic
        # c.post_id = int(str(postId))
        c.user = request.user
        c.save()

        print('\n\n\n')
       

    return HttpResponse("note")

def ajax_deletenote(request):
    print ("\n............deletenote ajax is called....\n")
    if (request.method =='POST'):
        noteId = request.POST.get('noteId', 'no comment')
        #userId = request.POST.get('userId', 'no user id')
        # reading_content_id = request.POST.get('reading_content_id', 'no reading_content_id')

        #print ("post id is: ..........." + postId)
        # print (note)
        # print (reading_content_id)
        c = ContentNotes.objects.get(id = int(str(noteId)))
        # if (c):
        #     c = c[0]
        # print (c.user)
        # print (request.user)
        if (c.user == request.user):
            c.delete()
            return HttpResponse("deletenote")

        # c.user = request.user

        # print("\n reading_content_id: \n" +  str(reading_content_id))
        # print (reading_content_id)
        # con = ReadingContent.objects.get(id=int(reading_content_id))
        # c.content = con
        # # c.post_id = int(str(postId))
        # c.user = request.user
        #c.save()

        #print('\n\n\n')
       

    return HttpResponse("deletenote_failed")
       

def ajax_addcomment(request):

    print ("in ajax add comment function")

    if (request.method =='POST'):
        comment = request.POST.get('comment', 'no comment')
        #userId = request.POST.get('userId', 'no user id')
        postId = request.POST.get('postId', 'no post id')

        print ("post id is: ..........." + postId)
        
        c = ContentComment(comment_text=str(comment))
        c.user = request.user
        c.content_id = int(str(postId))
        c.update_date()
        c.save()

        print('\n\n\n')
       



        data = {}
        data['task'] = 'add_comment'
        data['id'] = c.id
        data['user'] = getString(request.user.first_name + "  " +  request.user.last_name )
        data['pub_date'] = str(c.pub_date)
        data['comment_text'] = c.comment_text

        return HttpResponse(json.dumps(data), content_type = "application/json")

    return HttpResponse("comment")



def ajax_deletecomment(request):
    print ("\n............deletecomment ajax is called....\n")
    if (request.method =='POST'):
        commentId = request.POST.get('commentId', '')

        c = ContentComment.objects.get(id = int(str(commentId)))

        if (c.user == request.user):
            c.delete()
            return HttpResponse("deletecomment")

       

    return HttpResponse("deletecomment_failed")













def ajax_addmcq(request):

    if (request.method =='POST'):
        qid = request.POST.get('qid', '')
      
        c = Marked_Mcq(user= request.user)
        c.mcq_question_id = int(str(qid))

        c.save()

        print('\n\n\n')
       

    return HttpResponse("mcq")



def ajax_reportmcq(request):

    if (request.method =='POST'):
        qid = request.POST.get('qid', '')
        report_text = request.POST.get('report_text', '')      

        print ("********** report text")
        print (report_text)

        report = Report_Mcq_Question.objects.filter(user=request.user, mcq_question__id=int(qid)).first()


        if (not report):
            report = Report_Mcq_Question(user=request.user)
            report.mcq_question_id = int (qid)
            

        report.report_text = report_text
        report.save()
        report.update_date()



        #  = Marked_Mcq(user= request.user)
        # c.mcq_question_id = int(str(qid))

        # c.save()

        # print('\n\n\n')
       

    return HttpResponse("reportmcq")






def ajax_addquestion(request):

    if (request.method =='POST'):
        qid = request.POST.get('qid', '')
        #userId = request.POST.get('userId', 'no user id')
        # postId = request.POST.get('postId', 'no post')

        # if (postId == 'no post'):
        #     return HttpResponse("mcq already added")

        # print ("post id is: ..........." + postId)

   
        mqq = Marked_Quick_Question(user= request.user)

        mqq.quick_question_id = int(str(qid))

        # c.content_id = int(str(postId))
        mqq.save()

        print('\n\n\n')
       

    return HttpResponse("question")










def ajax_deletemcq(request):

    if (request.method =='POST'):


        qid = request.POST.get('qid', '')
        #userId = request.POST.get('userId', 'no user id')
        # postId = request.POST.get('postId', 'no post')

        # print ("post id is: ..........." + postId)
        # print ("qid id is: ..........." + qid)
        # print ("usesr id Is: " + str(request.user.id))

        # if (not postId == 'no post'):       
        # c = ContentMarkedMcq.objects.filter(mcq_question_id = int(str(qid)), 
        #     user=request.user, content_id=int(str(postId)))


        content_marked_mcq = Marked_Mcq.objects.filter(mcq_question_id = int(str(qid)), 
            user=request.user)

        if (content_marked_mcq):
            content_marked_mcq.delete()


        # print ("these mcqs will be removed from marked mcq")
        # print (content_marked_mcq)

        # for c in content_marked_mcq:
        #     c.delete()
        #     return HttpResponse("deletemcq")
        # if (c is not None):


        # else:
        #     content_marked_mcq = ContentMarkedMcq.objects.filter(mcq_question_id = int(str(qid)), 
        #         user=request.user)

        #     print ("\n*********** about to delete a list of mcq")
        #     print (content_marked_mcq)

        #     for c in content_marked_mcq:
        #         c.delete()

        return HttpResponse("deletemcq")











def ajax_deletequestion(request):

    if (request.method =='POST'):


        qid = request.POST.get('qid', '')
        #userId = request.POST.get('userId', 'no user id')
        # postId = request.POST.get('postId', 'no post')

        # print ("post id is: ..........." + postId)
        print ("qid id is: ..........." + qid)
        print ("usesr id Is: " + str(request.user.id))

        # if (not postId == 'no post'):       
        # c = ContentMarkedMcq.objects.filter(mcq_question_id = int(str(qid)), 
        #     user=request.user, content_id=int(str(postId)))


        quick_question = Marked_Quick_Question.objects.filter(quick_question_id = int(str(qid)), 
            user=request.user)


        if (quick_question):
            quick_question.delete()

      
        
       

    return HttpResponse("deletequestion")






def ajax_add_marked_text(request):

    if (request.method =='POST'):
        text = request.POST.get('text', 'no comment')
        #userId = request.POST.get('userId', 'no user id')
        postId = request.POST.get('postId', 'no post id')
        postId = int(str(postId))


        # print ("post id is: ..........." + str(postId))
        # print (text)
        content_marked_text = ContentMarkedText.objects.filter(user = request.user, content_id = postId)



        if (content_marked_text):
            content_marked_text = content_marked_text[0]
            content_marked_text.marked_text = text
            content_marked_text.save()

        else:        
            c = ContentMarkedText(marked_text = text)
            c.user = request.user
            c.content_id = int(str(postId))
            c.save()

        print('\n\n\n')
       

    return HttpResponse("marked_text")


def ajax_delete_marked_text(request):

    if (request.method =='POST'):
        text = request.POST.get('text', 'no comment')
        #userId = request.POST.get('userId', 'no user id')
        postId = request.POST.get('postId', 'no post id')
        postId = int(str(postId))


        print ("post id is: ..........." + str(postId))
        # print (text)
        content_marked_text = ContentMarkedText.objects.filter(user = request.user, content_id = postId)

        for c in content_marked_text:
            c.delete()



        print('\n\n\n')
       

    return HttpResponse("delete_marked_text")

# @login_required(login_url="/exam/login/")
# def ajax(request):

#     print ("\n\n in ajax function \n\n")

#     if request.method == 'POST':
#         text = request.POST.get('text2', 'No data has been sent')
#         aj = MarkedText(marked_text=text)
#         aj.user = request.user
#         aj.save()

#         return HttpResponse("ajax successful sent from the dajngo ajax function")
    

#     return render(request, 'exam/ajax.html')












# return render(request, 'blog/post_details.html', {'post' : post, 'comment': comment})

# def readingcontent(request, topic_id, subtopic1_id, subtopic2_id):
#   subtopic2 = SubTopic2.objects.filter(subtopic1=subtopic1_id)

#   return render (request, 'readingmaterial/subtopic2.html', {'subtopic2': subtopic2})
#     #return HttpResponse("Hello, world. You're at the .... reading material ..... index.")

# # return render(request, 'blog/post_details.html', {'post' : post, 'comment': comment})


