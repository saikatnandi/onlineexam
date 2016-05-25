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



def index(request):
    st = "<h1> this is blog home page </h1>"
    if not request.user.is_authenticated():
        st += "noooooooooooooooooooooooooooooot authenticated<br><br>"
    else:
        st += "authenticated..................................user name: " + request.user.username + "<br><br>"
        st += "and user id is:" + str(request.user.id) + " <br>"


    st += "<br>Hello, world. You're at the exam index method index."
    return render(request, 'blog/index.html', {'data' : st})





def post_details(request, post_id):
    post = Post.objects.get(id = post_id)
    comment = Comment.objects.filter(post = post)
    blog_tag = ""
    if (post):
        blog_tag = Tag.objects.filter(post = post)


    return render(request, 'blog/post_details.html', 
        {'post' : post, 'comment': comment, 'post_id': post_id,
         'blog_tag' : blog_tag

        }

        )




@login_required(login_url="/login/")
def writepost(request):
    s = ""
    form = Writepost_Form()

    if (request.method == 'POST'):
        form = Writepost_Form(request.POST, request.FILES)

        s += "the request is post <br>"
        if (form.is_valid()):
            s += "the request is valid<br>"
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            task.update_date()

            task.save()
            form.save(commit=True)

            return HttpResponse("the post is saved in the database")

   
    
    

    # c = {}
    # c.update(csrf(request))
    # c.update({'form':form})

    # return render_to_response( 'blog/writepost.html', c)

    return render (request, 'blog/writepost.html', {'form': form}) 




def allpost(request):

	blog = Post.objects.all().order_by("-pub_date")
	return render (request, 'blog/allpost.html', {'blog': blog}) 


def mypost(request):

    blog = Post.objects.filter(user=request.user).order_by("-pub_date")
    return render (request, 'blog/allpost.html', {'blog': blog}) 



def mypost_edit(request, post_id):
    s = ""
    form = Writepost_Form()


    if (request.method == 'POST'):
        post = Post.objects.get(id = post_id, user=request.user)
        form = Writepost_Form(request.POST, request.FILES, instance=post)

        s += "the request is post <br>"

        # print ("\n\n\n ****** trying to save the form")
        if (form.is_valid()):
            s += "the request is valid<br>"
            task = form.save(commit=False)

            task.user = request.user
            task.save()
            task.update_date()

            task.save()
            form.save(commit=True)

            return HttpResponse("the post is saved in the database")

    else:
        form=Writepost_Form(instance=Post.objects.get(pk=post_id))


    return render (request, 'blog/writepost.html', {'form': form}) 







def allpost_by_taglist(request, tag_id):
    # tag = Tag.objects.

    blog = Post.objects.filter(tag__id = int(str(tag_id)))
    return render (request, 'blog/allpost.html', {'blog': blog}) 




def taglist(request):

    tag = Tag.objects.all()
    return render (request, 'blog/taglist.html', {'taglist': tag}) 






def ajax_comment(request):

    if (request.method =='POST'):
        comment = request.POST.get('comment', 'no comment')
        #userId = request.POST.get('userId', 'no user id')
        postId = request.POST.get('postId', 'no post id')

        print ("post id is: ..........." + postId)
        
        c = Comment(comment_text=str(comment))
        c.user = request.user
        c.post_id = int(str(postId))
        c.update_date()
        c.save()

        print('\n\n\n')
       

    return HttpResponse("comment")



def ajax_deletecomment(request):

    if (request.method =='POST'):
        commentId = request.POST.get('commentId', '')
        #userId = request.POST.get('userId', 'no user id')
        c = Comment.objects.get(id = int(str(commentId)))

        if (c.user == request.user):
            c.delete()
            return HttpResponse("deletecomment")       

    return HttpResponse("deletecomment_failed")



