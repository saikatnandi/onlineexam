from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
   

    Tag_text = models.CharField(max_length=200)
    

    def __str__(self):
    	return self.Tag_text

class Question(models.Model):
    tags = models.ManyToManyField(Tag)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
   

    def __str__(self):
    	return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, blank=True, null=True)
    answer_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', blank=True, null=True)

    def __str__(self):
    	return self.answer_text




