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
from announcement.models import *
from django.db.models import Q



def index(request):

    link_topic = Link_Topic.objects.all()
    links = Link.objects.filter(link_topic__isnull = True)

    now = timezone.now()
    announcement = Announcement.objects.filter( Q(start_date__isnull = True) | Q(start_date__lte=now))
    announcement = announcement.filter(Q(end_date__isnull = True) | Q(end_date__gte = now))
    
    return render(request, 'links/index.html', {
    	'link_topic' : link_topic,
    	'links' : links,
    	'announcement' : announcement,

    	})



def link_details(request, link_id):
    link = Link.objects.get(id = link_id)
    now = timezone.now()
    announcement = Announcement.objects.filter( Q(start_date__isnull = True) | Q(start_date__lte=now))
    announcement = announcement.filter(Q(end_date__isnull = True) | Q(end_date__gte = now))

    return render(request, 'links/link_details.html', 
        {
        'link' : link , 'announcement' : announcement
        }

        )


def topic_details(request, topic_id):
    links = Link.objects.filter(link_topic = topic_id)
    now = timezone.now()
    announcement = Announcement.objects.filter( Q(start_date__isnull = True) | Q(start_date__lte=now))
    announcement = announcement.filter(Q(end_date__isnull = True) | Q(end_date__gte = now))

    return render(request, 'links/topic_details.html', 
        {
        'links' : links , 'announcement' : announcement
        }

        )