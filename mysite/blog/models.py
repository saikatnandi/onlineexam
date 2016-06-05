from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import admin
from ckeditor.fields import *
from django.utils.safestring import SafeUnicode
from ckeditor_uploader.fields import *
# Create your models here.






class Tag(models.Model):
	tag_text = models.CharField(max_length=100)

	def __unicode__(self):
		return self.tag_text



class Post(models.Model):
    title_text = models.CharField("Title: ",max_length=200)
    # post_body = RichTextField("Body Of Post", blank=True, null=True)
    # post_body = RichTextField("Body Of Post", blank=True, null=True)

    post_body = RichTextUploadingField("Body Of Post", blank=True, null=True)


    # post_body2 = RichTextField(blank=True, null=True)

    user = models.ForeignKey(User)
    tag = models.ManyToManyField(Tag, blank=True, null=True)

    image1 = models.ImageField(upload_to='images/blog', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/blog', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/blog', blank=True, null=True)

    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)

    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()
        self.save() 

    def __unicode__(self):
        return (self.title_text) 



class Comment(models.Model):
    comment_text = models.TextField()
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)

    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()
        self.save() 


    def __unicode__(self):
        s = 'U: ' + str(self.user.id)
        s += str(self.comment_text)
        return s

