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
# from announcement.models import *


# @login_required(login_url="/login/")
# def index(request):


#     return render(request, 'dashboard/index.html', {
#         'data': "alamin",

#         })


def getString(title):
    try:
        title = str(title)
    except Exception:
        title = title.encode('UTF8')

    print ("\n ********** retirng strign: " + title)
    return title



@login_required(login_url="/login/")
def ajax_addmessage(request):

    if (request.method =='POST'):
        message = request.POST.get('message', '')
        #userId = request.POST.get('userId', 'no user id')
        # postId = request.POST.get('postId', 'no post id')

        # print ("post id is: ..........." + postId)
        




        c = Message(message_text=getString(message))
        c.user = request.user
        c.is_receiver = False
        # c.content_id = int(str(postId))
        c.update_date()
        c.save()

        # print('\n\n\n')
       

    return HttpResponse("message")

