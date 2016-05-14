from __future__ import unicode_literals
from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from links.models import *
from qa1.models import *
from readingmaterial.models import *
from notice.models import *





class Announcement(models.Model):  
    announcement_text = models.CharField(max_length=200, blank=True, null=True)       
    url = models.CharField(max_length=200, blank=True, null=True)       


    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)
  
    start_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    end_date = models.DateTimeField('Editing Date: ', blank=True, null=True)


    uploader = models.ForeignKey(User, blank=True, null=True)

  
    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()

        self.save() 




        
    def __unicode__(self):
        return self.announcement_text

    class Meta:
        verbose_name="Important Accouncement"




class User_Notification(models.Model):  
    notification_text = models.CharField(max_length=200)       
    url = models.CharField(max_length=200, blank=True, null=True)       


    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)
    is_forall = models.BooleanField("For All User",default=True)

  
    # start_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    # end_date = models.DateTimeField('Editing Date: ', blank=True, null=True)


    uploader = models.ForeignKey(User, blank=True, null=True)

    question_set = models.ForeignKey(Question_Set, blank=True, null=True)
    reading_content = models.ForeignKey(ReadingContent, blank=True, null=True)
    notice = models.ForeignKey(Notice, blank=True, null=True)
    link = models.ForeignKey(Link, blank=True, null=True)
  
    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()

        self.save() 




        
    def __unicode__(self):
        return self.notification_text

    class Meta:
        verbose_name="Notication For User"


