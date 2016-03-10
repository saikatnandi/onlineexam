from __future__ import unicode_literals

from django.db import models
from django import forms
from readingmaterial.models import *
from qa1.models import *
from django.utils import timezone

# Create your models here.

class Upload_Question_From_Excel(models.Model):
    content = models.ForeignKey(ReadingContent, null=True, blank=True)
    tag = models.CharField(max_length=200, null=True, blank=True)
    excel_file = models.FileField(upload_to='resource_files/' ,blank=True, null=True)

    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)

    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()

        self.save()  

    def __unicode__(self):

        return  str(self.content)


    class Meta:
        permissions = (
            ('excel_upload', 'excel_upload'),
           
        )


class Upload_Question_Set_From_Excel(models.Model):
    question_set = models.ForeignKey(Question_Set, null=True, blank=True)
    tag = models.CharField(max_length=100, null=True, blank=True)
    excel_file = models.FileField(upload_to='resource_files/' ,blank=True, null=True)

    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)

    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()

        self.save()  

    def __unicode__(self):

        return  str(self.content)


    class Meta:
        permissions = (
            ('excel_question_set_upload', 'excel_question_set_upload'),
           
        )