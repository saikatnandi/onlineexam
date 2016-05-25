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
from django.core.mail import send_mail

from models import *



@login_required(login_url="/login/")
def  index(request):
    subscription = Subscription_Plan.objects.all().order_by("subscription_fee")



    return render(request, 'subscription/index.html', {
    	'subscription': subscription,
 

    	})


@login_required(login_url="/login/")
def subscribe_request(request, plan_id):

    # print (plan_id)

    subscription_request = Subscription_Request.objects.filter(user=request.user, 
        subscription_plan_id=plan_id, is_confirmed=False)
    subscription_request = subscription_request.order_by('-request_date')
    # print (subscription)
    flag = False
    if (subscription_request):
        subscription_request = subscription_request[0]
        subscription_request.request_date = timezone.now()
        subscription_request.save()
        flag = True
        # if (not subscription.is_confirmed):
        #     flag = True


        # t =   timezone.now() - subscription.request_date
        # # print ("************** time")
        # print (t.days)
        # # if (subscription.request_date )
        # if (t.days < 7):
        #     flag = True





    if (not flag):
        subscription_request = Subscription_Request(user = request.user)
        # print ("******printing plan id")
        # print (plan_id)
        plan = Subscription_Plan.objects.get(id = plan_id)
        subscription_request.subscription_plan = plan
        # subscription.no_of_random_question = plan.no_of_random_question
        # subscription.no_of_exam_per_day = plan.no_of_exam_per_day

        # print (subscribe.subscribe_plan)
        subscription_request.request_date = timezone.now()


        subscription_request.save()
        subscription_request.token = "TOKEN" + str(subscription_request.id)
        subscription_request.save()


    return render(request, 'subscription/subscribe.html', {
        'subscription': subscription_request,
 

        })










# def  my_send_mail(request):

#     send_mail('Testing Mail', 'Here is the message.', 'abc@gmail.com',
#     ['mdabdullahalalaminp@gmail.com'], fail_silently=False)

#     return HttpResponse("Mail Sending Okay")

