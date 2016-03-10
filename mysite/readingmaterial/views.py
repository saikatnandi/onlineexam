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
from django.core.context_processors import csrf



def index(request):
	reading_topic = ReadingTopic.objects.all()

	return render(request, 'readingmaterial/index.html',{'reading_topic': reading_topic})

def subtopic1(request, topic_id):
	subtopic1 = SubTopic1.objects.filter(topic=topic_id)

	return render (request, 'readingmaterial/subtopic1.html', {'subtopic1': subtopic1})




def reading_content_list(request, topic_id, subtopic1_id):
	readingcontentlist = ReadingContent.objects.filter(subtopic1=subtopic1_id)


	return render (request, 'readingmaterial/readingcontentlist.html', {'readingcontentlist': readingcontentlist})
    #return HttpResponse("Hello, world. You're at the .... reading material ..... index.")


def getContentMarkedMcqString(content_marked_mcq):
    cmm = ""
    for m in content_marked_mcq:
        if (m.mcq_question is not None):
            cmm += str(m.mcq_question.id) + ', '  

    return cmm 

def reading_content_details(request, topic_id, subtopic1_id, reading_content_id):
    readingcontent = ReadingContent.objects.get(id=reading_content_id)
    readingcontent_text = ""
    content_marked_mcq = ""

    if (request.user.is_authenticated()):
        print ("*********authenticated user*********")
        readingcontent_text = ContentMarkedText.objects.filter(user = request.user, content_id = reading_content_id)
    
        content_marked_mcq = ContentMarkedMcq.objects.filter( user=request.user)

    readingcontentlist = ReadingContent.objects.filter(subtopic1=subtopic1_id)


    comment = ContentComment.objects.filter(content = readingcontent)
    mcq_question = Mcq_Question.objects.filter(readingcontent__id=reading_content_id)
    # content_marked_mcq = ContentMarkedMcq.objects.filter(content=readingcontent, user=request.user)
    

    cmm = ""
   

    # for m in content_marked_mcq:
    #     if (m.mcq_question is not None):
    #         cmm += str(m.mcq_question.id) + ', '

    print ("\n cmm is: %s" % cmm)
    note = None
    if (request.user.is_authenticated()):
        cmm = getContentMarkedMcqString(content_marked_mcq)
        note = ContentNotes.objects.filter(user=request.user, content=reading_content_id)


    print ("*****going to return template\n")
    return render (request, 'readingmaterial/reading_content_details.html', 
        {'readingcontent': readingcontent, 'readingcontentlist': readingcontentlist,
        'reading_content_id': reading_content_id,'note': note, 'comment': comment,
        'mcq_question': mcq_question, 'content_marked_mcq_string': cmm,
        'readingcontent_text': readingcontent_text,
        })
    #return HttpResponse("Hello, world. You're at the .... reading material ..... index.")



@login_required(login_url="/login/")
def dashboard(request):

    note = ContentNotes.objects.filter(user=request.user)
    data = ContentNotes.objects.filter(content__subtopic1__topic=2)
    n = ""
    
    if (note):
        n = note[0]

    li = [2,3,4,5]

    reading_topic = ReadingTopic.objects.filter(subtopic1__readingcontent__contentnotes__user = request.user).distinct()
    print (reading_topic)
    marked_mcq =""
    # marked_mcq = Mcq_Question.objects.filter(readingcontent__contentmarkedmcq__user=request.user).distinct()
    mcq_question = Mcq_Question.objects.filter(contentmarkedmcq__user=request.user).distinct()
    # mcq_question = Mcq_Question.objects.filter(readingcontent__contentmarkedmcq__user = request.user)
    # # mcq_question = ContentMarkedMcq.objects.filter(user = request.user)
    marked_mcq_topic = ReadingTopic.objects.filter(subtopic1__readingcontent__contentmarkedmcq__user = request.user).distinct()
 
    marked_mcq_topic = ReadingTopic.objects.filter(subtopic1__readingcontent__mcq_question__in = mcq_question).distinct()
    marked_mcq = ContentMarkedMcq.objects.filter(user = request.user)
    # marked_mcq_topic = ReadingTopic.objects.filter(subtopic1__readingcontent__contentmarkedmcq__user = request.user)


    cmm = ""
    # cmm = getContentMarkedMcqString(content_marked_mcq)

    for m in marked_mcq:
        if (m is not None):
            cmm += str(m.mcq_question.id) + ', '


    return render(request, 'readingmaterial/dashboard.html', {
        'note': note, 'data': data, 'reading_topic': reading_topic,
        'mcq_question': mcq_question, 'content_marked_mcq_string': cmm,
        'marked_mcq': marked_mcq, 'marked_mcq_topic': marked_mcq_topic,
        })















def ajax_addnote(request):
    print ("\n............addnote ajax is called....\n")
    if (request.method =='POST'):
        note = request.POST.get('note', 'no comment')
        #userId = request.POST.get('userId', 'no user id')
        reading_content_id = request.POST.get('reading_content_id', 'no reading_content_id')

        #print ("post id is: ..........." + postId)
        # print (note)
        # print (reading_content_id)
        c = ContentNotes(content_notes=str(note))
        c.user = request.user

        print("\n reading_content_id: \n" +  str(reading_content_id))
        print (reading_content_id)
        con = ReadingContent.objects.get(id=int(reading_content_id))
        c.content = con
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
       

    return HttpResponse("comment")

def ajax_addmcq(request):

    if (request.method =='POST'):
        qid = request.POST.get('qid', 'no comment')
        #userId = request.POST.get('userId', 'no user id')
        # postId = request.POST.get('postId', 'no post')

        # if (postId == 'no post'):
        #     return HttpResponse("mcq already added")

        # print ("post id is: ..........." + postId)

        content_marked_mcq = ContentMarkedMcq.objects.filter(user=request.user, mcq_question_id = qid)
        if (not content_marked_mcq):       
            c = ContentMarkedMcq(user= request.user)
            c.mcq_question_id = int(str(qid))
            content_list = ReadingContent.objects.filter(mcq_question__id = qid)
            for cl in content_list:
                c.content = cl
            # c.content_id = int(str(postId))
            c.save()

        print('\n\n\n')
       

    return HttpResponse("mcq")


def ajax_deletemcq(request):

    if (request.method =='POST'):


        qid = request.POST.get('qid', 'no comment')
        #userId = request.POST.get('userId', 'no user id')
        # postId = request.POST.get('postId', 'no post')

        # print ("post id is: ..........." + postId)
        print ("qid id is: ..........." + qid)
        print ("usesr id Is: " + str(request.user.id))

        # if (not postId == 'no post'):       
        # c = ContentMarkedMcq.objects.filter(mcq_question_id = int(str(qid)), 
        #     user=request.user, content_id=int(str(postId)))


        content_marked_mcq = ContentMarkedMcq.objects.filter(mcq_question_id = int(str(qid)), 
            user=request.user)


        print ("these mcqs will be removed from marked mcq")
        print (content_marked_mcq)

        for c in content_marked_mcq:
            c.delete()
            return HttpResponse("deletemcq")
        # if (c is not None):


        # else:
        #     content_marked_mcq = ContentMarkedMcq.objects.filter(mcq_question_id = int(str(qid)), 
        #         user=request.user)

        #     print ("\n*********** about to delete a list of mcq")
        #     print (content_marked_mcq)

        #     for c in content_marked_mcq:
        #         c.delete()

        return HttpResponse("deletemcq")






        
        
       

    return HttpResponse("deletemcq_failed")

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
# 	subtopic2 = SubTopic2.objects.filter(subtopic1=subtopic1_id)

# 	return render (request, 'readingmaterial/subtopic2.html', {'subtopic2': subtopic2})
#     #return HttpResponse("Hello, world. You're at the .... reading material ..... index.")

# # return render(request, 'blog/post_details.html', {'post' : post, 'comment': comment})


