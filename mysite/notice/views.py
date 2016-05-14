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



def index(request):

    notice_topic = Notice_Topic.objects.all()
    notices = Notice.objects.filter(notice_topic__isnull = True)

    return render(request, 'notice/index.html', {
    	'notice_topic' : notice_topic,
    	'notices' : notices

    	})



def notice_details(request, notice_id):
    notice = Notice.objects.get(id = notice_id)

    return render(request, 'notice/notice_details.html', 
        {
        'notice' : notice
        }

        )


def topic_details(request, topic_id):
    notices = Notice.objects.filter(notice_topic = topic_id)

    return render(request, 'notice/topic_details.html', 
        {
        'notices' : notices
        }

        )



