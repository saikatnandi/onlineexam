from __future__ import unicode_literals
from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User




class Subscription_Plan(models.Model):   
    subscription_plan_title = models.CharField(max_length=200)       
    subscription_fee = models.IntegerField("Subscription Fee", default=0) 
    subscription_duration = models.IntegerField("Subscription Duration(In Days)", default=-1) 
    can_create_blog_tag = models.BooleanField("Can Create Blog Tag",default=False)
    no_of_exam_per_day = models.IntegerField("No Of Exam Per Day",
     default=-1)
    no_of_random_question  = models.IntegerField("No Of Random Question",
     default=0)
    bkash_no = models.CharField(max_length=200, default="01521253206")



    def __unicode__(self):
        return self.subscription_plan_title

    class Meta:
        verbose_name="Regular Subscription Plan"



class Subscription(models.Model):   
    user = models.ForeignKey(User)
    subscription_plan = models.ForeignKey(Subscription_Plan)


    # token = models.CharField(max_length=200, blank=True, null=True)
    # request_date = models.DateTimeField('Request Date: ', default = timezone.now())
    start_date = models.DateTimeField('Start Date: ', blank=True, null=True)
    end_date = models.DateTimeField('End Date: ', blank=True, null=True)

    # is_confirmed = models.BooleanField("Conform",default=False)
    is_valid = models.BooleanField("Valid",default=False)

    no_of_exam_per_day = models.IntegerField("No Of Exam Per Day",
     default=-1)
    no_of_random_question  = models.IntegerField("No Of Random Question",
     default=0)

    
    def update_validity(self):
        if (self.is_valid):            
            if ( self.end_date < timezone.now()):
                self.is_valid = False
                self.save()



        # self.save()    
    

    def __unicode__(self):
        return str(self.user) + " " + str(self.subscription_plan)

    class Meta:
        verbose_name="Subscription Of Regular Plan"
        # unique_together = ('user', 'subscription_plan', 'is_valid', 'is_confirmed')



class Subscription_Request(models.Model):   
    user = models.ForeignKey(User)
    subscription_plan = models.ForeignKey(Subscription_Plan)


    token = models.CharField(max_length=200, blank=True, null=True)
    request_date = models.DateTimeField('Request Date: ', default = timezone.now())
    # start_date = models.DateTimeField('Start Date: ', blank=True, null=True)
    # end_date = models.DateTimeField('End Date: ', blank=True, null=True)

    is_confirmed = models.BooleanField("Conform",default=False)
    is_valid = models.BooleanField("Valid",default=True)

    # no_of_exam_per_day = models.IntegerField("No Of Exam Per Day",
    #  default=-1)
    # no_of_random_question  = models.IntegerField("No Of Random Question",
    #  default=0)

    
    def update_validity(self):
        if (self.is_valid):
            if (self.is_confirmed):
                self.is_valid = False
                self.save()

        # self.save()    
    

    def __unicode__(self):
        return str(self.user) + " " + str(self.subscription_plan)

    class Meta:
        verbose_name="Subscription Request"
        # unique_together = ('user', 'subscription_plan', 'is_valid', 'is_confirmed')




# class Special_Plan(models.Model):   
#     special_plan_title = models.CharField(max_length=200)       
#     special_plan_fee = models.IntegerField("Subscription Fee", default=0) 

#     bkash_no = models.CharField(max_length=200, default="01521253206")


    

#     def __unicode__(self):
#         return self.special_plan_title

#     class Meta:
#         verbose_name="Special Subscription Plan"
















# class Subscription_Special_Plan(models.Model):   
#     user = models.ForeignKey(User)
#     special_plan = models.ForeignKey(Special_Plan)

    
#     token = models.CharField(max_length=200, blank=True, null=True)
#     request_date = models.DateTimeField('Request Date: ', default = timezone.now())
#     is_confirmed = models.BooleanField("Conformation",default=False)

    

#     def __unicode__(self):
#         return str(self.user) + " " + str(self.special_plan)

#     class Meta:
#         verbose_name="Subscription Of Special Plan"