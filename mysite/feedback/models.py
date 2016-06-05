from __future__ import unicode_literals
from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
# from links.models import *
from qa1.models import *
from readingmaterial.models import *
# from notice.models import *






class Message(models.Model):  
    message_text = models.CharField(max_length=200)       
    # url = models.CharField(max_length=200, blank=True, null=True)       


    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)
  
    # start_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    # end_date = models.DateTimeField('Editing Date: ', blank=True, null=True)


    user = models.ForeignKey(User)
    # user_id = models.IntegerField("User Id", blank=True, null=True) 

    is_receiver = models.BooleanField("Is This User Receiver Or Sender",default=True)

    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()

        self.save() 




        
    def __unicode__(self):
        return self.message_text

    class Meta:
        verbose_name="Message/Objection From User"



class Report_Mcq_Question(models.Model):  
    report_text = models.CharField(max_length=200, blank=True, null=True)    
    # url = models.CharField(max_length=200, blank=True, null=True)       


    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)
    # is_forall = models.BooleanField("For All User",default=True)


    user = models.ForeignKey(User)
    mcq_question = models.ForeignKey(Mcq_Question)
    # link = models.ForeignKey(Link, blank=True, null=True)
  
    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()

        self.save() 




        
    def __unicode__(self):
        return self.report_text

    class Meta:
        verbose_name="Report/Correction From User For MCQ"
        unique_together = ('user', 'mcq_question', )




class Report_Quick_Question(models.Model):  
    report_text = models.CharField(max_length=200, blank=True, null=True)    
    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)
    # is_forall = models.BooleanField("For All User",default=True)


    user = models.ForeignKey(User)

    quick_question = models.ForeignKey(Quick_Question)
    # reading_content = models.ForeignKey(ReadingContent, blank=True, null=True)
    mcq_question = models.ForeignKey(Mcq_Question, blank=True, null=True)
    # link = models.ForeignKey(Link, blank=True, null=True)
  
    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()

        self.save() 




        
    def __unicode__(self):
        return self.report_text

    class Meta:
        verbose_name="Report/Correction  From User Quick Question"
        unique_together = ('user', 'quick_question', )


