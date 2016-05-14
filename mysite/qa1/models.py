from __future__ import unicode_literals
from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# from readingmaterial.models import ReadingTopic
from readingmaterial.models import SubTopic1
from readingmaterial.models import *
from subscription.models import *


# class ReadingContentInline(admin.TabularInline):
#     model = ReadingContent
#     extra = 0



class Question_Topic(models.Model):   
    question_topic_text = models.CharField(max_length=200, blank=True, null=True)       
    is_reading_content = models.BooleanField("Is Topic Wise",default=False)
    def __unicode__(self):
        return self.question_topic_text

    class Meta:
        verbose_name="Question Topic List"



# class Subject(models.Model):
#     subject_text = models.CharField(max_length=100)
#     def __unicode__(self):
#         return self.subject_text

# class Tag(models.Model):
#     tag_text = models.CharField(max_length=30)
#     def __unicode__(self):
#         return self.tag_text



class Mcq_Question(models.Model):

    # question_set = models.ManyToManyField(Question_Set, blank=True, null=True) 
    # subject_set = models.ManyToManyField(Subject, blank=True, null=True)
    # tag_set = models.ManyToManyField(Tag, blank=True, null=True)

    question_text = models.CharField(max_length=400)   
    mcq_image = models.ImageField(upload_to='images/mcq/', blank=True, null=True)
    choice_a =  models.CharField(max_length=200, blank=True, null=True) 
    choice_b =  models.CharField(max_length=200, blank=True, null=True) 
    choice_c =  models.CharField(max_length=200, blank=True, null=True) 
    choice_d =  models.CharField(max_length=200, blank=True, null=True) 
    choice_e =  models.CharField(max_length=200, blank=True, null=True) 
    choice_f =  models.CharField(max_length=200, blank=True, null=True) 
    

    mcq_answer = models.CharField(max_length=200, blank=True, null=True)  
    mcq_answer2 = models.CharField(max_length=200, blank=True, null=True)

    tag1 = models.CharField(max_length = 100, blank=True, null=True)
    tag2 = models.CharField(max_length=100, blank=True, null=True)
    tag3 = models.CharField(max_length=100, blank=True, null=True)
    tag4 = models.CharField(max_length=100, blank=True, null=True)
    tag5 = models.CharField(max_length=100, blank=True, null=True)

    tag_topic = models.CharField(max_length=100, blank=True, null=True)
    tag_sub_topic = models.CharField(max_length=100, blank=True, null=True)
    tag_content = models.CharField(max_length=100, blank=True, null=True)

    tag_inconsistent = models.CharField(max_length=200, blank=True, null=True)






    explanation_text = models.TextField( blank=True, null=True)
    explanation_image = models.ImageField(upload_to='images/mcq/', blank=True, null=True)

    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)

    uploader = models.ForeignKey(User, blank=True, null=True)

    subtopic1 = models.ForeignKey(SubTopic1, blank=True, null=True)
    reading_topic = models.ForeignKey(ReadingTopic, blank=True, null=True)


    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()
        self.save()  





    def __unicode__(self):
        # s = ""
        # s = "Q: " + str(self.question_text)
        # s += " Tag: " + str(self.tag1)
        #return "%50s %10s %10s %10s" % (self.question_text, self.tag1, self.tag2, self.tag3)
        # s = "{:30}  {:10} {:10}".format(self.question_text, self.tag1, self.tag2)
        # s = "..        alamin........  qartqewrewerwrewqrrqewreqwerq34521erfdsasdfasdfdfgwe45243erafadsfq435   b"
       
        # s = 'Q: %s ..|||.. .t_topic:%s .t_sub_topic:%s .t_content:%s .t1:%s .t2:%s .t3:%s .t4:%s .t5:%s' % (self.question_text,
        #  self.tag_topic, self.tag_sub_topic, 
        #     self.tag_content, self.tag1, self.tag2, self.tag3, self.tag4, self.tag5)


        return  self.question_text

    class Meta:
        verbose_name=" Individual MCQ Questions "


class Question_Set(models.Model):  
    question_set_text = models.CharField(max_length=200, verbose_name="Question Set")  
    question_topic = models.ForeignKey(Question_Topic,blank=True, null=True) 
    
    reading_content = models.ForeignKey(ReadingContent, blank=True, null=True)
    subtopic1 = models.ForeignKey(SubTopic1, blank=True, null=True, verbose_name="Sub Topic Name")
    reading_topic = models.ForeignKey(ReadingTopic,  blank=True, null=True)

    mcq_question = models.ManyToManyField(Mcq_Question, blank=True, null=True)  
    reading_content = models.ForeignKey(ReadingContent, blank=True, null=True)

    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)

    uploader = models.ForeignKey(User, blank=True, null=True)

    individual_mcq_marks = models.IntegerField("Individual Mcq Question Marks: ", default=1) 
    negative_marking_percentage = models.IntegerField("Percent Of Marks To Be Deducted For Wrong Answer: ", default=0) 

    individual_mcq_time = models.IntegerField("Individual Mcq Question Time In Second: ", default=60) 


    is_free = models.BooleanField("Is Free",default=True)
    subscription_plan = models.ManyToManyField(Subscription_Plan)
    special_plan = models.ManyToManyField(Special_Plan)
 

    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()

        self.save() 

        
    def __unicode__(self):
        return self.question_set_text

    class Meta:
        verbose_name="Question Set"

# class Question_Set2(models.Model):  
    
#     question_set2_text = models.CharField(max_length=200)  
#     mcq_question_set = models.ManyToManyField(Mcq_Question)


#     def __unicode__(self):
#         return self.question_set2_text


# class Image(models.Model):
#     image_text = models.CharField(max_length=30)
#     photo = models.ImageField(upload_to='images')

#     def __unicode__(self):
#         return self.image_text

class MarkedText(models.Model):
    marked_text = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, blank=True)


    def __unicode__(self):
        return self.marked_text



class Marked_Mcq(models.Model):
    user = models.ForeignKey(User)
    mcq_question = models.ForeignKey(Mcq_Question)
    # content = models.ForeignKey(ReadingContent, null=True, blank=True)

    # def __unicode__(self):
    #     return ("user: %s mcq_question: %s " %(self.user, self.mcq_question))

    class Meta:
        unique_together = ('user', 'mcq_question',)




class Question_Set_Result(models.Model):  
    user = models.ForeignKey(User)    
    question_set = models.ForeignKey(Question_Set)    


    start_date = models.DateTimeField('Publishing Date: ')
    finish_date = models.DateTimeField('Editing Date: ')

    marks =  models.FloatField(blank=True, null=True)
    position  =  models.IntegerField("Position", default=0) 


    def update_date(self):
        # if (not self.pub_date):
        #     self.pub_date = timezone.now()

        # self.edit_date = timezone.now()

        self.save() 
    # def update_position(self):
    #     pos = Question_Set_Result.objects.filter(question_set = self.question_set)
    #     pos = pos.filter(marks__gt=self.marks).count()

    #     print ("positon is: ")
    #     print (pos)
    #     self.positon = (pos+1)
    #     print (self.positon)
    #     self.save()



        
    def __unicode__(self):
        return self.question_set.question_set_text

    class Meta:
        verbose_name="Result"
        unique_together = ('user', 'question_set',)