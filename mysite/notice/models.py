from __future__ import unicode_literals
from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User




class Notice_Topic(models.Model):   
    notice_topic_text = models.CharField(max_length=200, blank=True, null=True)       

    def __unicode__(self):
        return self.notice_topic_text

    class Meta:
        verbose_name="Notice Topic List"

class Notice(models.Model):  
    notice_title = models.CharField(max_length=200, blank=True, null=True)       

    notice_text = models.TextField(max_length=200, blank=True, null=True, verbose_name="Notice ")  
    notice_topic = models.ForeignKey(Notice_Topic,blank=True, null=True) 

    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)
    
    image1 = models.ImageField(upload_to='images/notice/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/notice/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/notice/', blank=True, null=True)

    file1 = models.FileField(upload_to='files/notice/', blank=True, null=True)
    file2 = models.FileField(upload_to='files/notice/', blank=True, null=True)
    file3 = models.FileField(upload_to='files/notice/', blank=True, null=True)





    uploader = models.ForeignKey(User, blank=True, null=True)

  
    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()

        self.save() 




        
    def __unicode__(self):
        return self.notice_text

    class Meta:
        verbose_name="Notice"





# # class Subject(models.Model):
# #     subject_text = models.CharField(max_length=100)
# #     def __unicode__(self):
# #         return self.subject_text

# # class Tag(models.Model):
# #     tag_text = models.CharField(max_length=30)
# #     def __unicode__(self):
# #         return self.tag_text



# class Mcq_Question(models.Model):

#     # question_set = models.ManyToManyField(Question_Set, blank=True, null=True) 
#     # subject_set = models.ManyToManyField(Subject, blank=True, null=True)
#     # tag_set = models.ManyToManyField(Tag, blank=True, null=True)

#     question_text = models.CharField(max_length=400)   
#     mcq_image = models.ImageField(upload_to='images/mcq/', blank=True, null=True)
#     choice_a =  models.CharField(max_length=200, blank=True, null=True) 
#     choice_b =  models.CharField(max_length=200, blank=True, null=True) 
#     choice_c =  models.CharField(max_length=200, blank=True, null=True) 
#     choice_d =  models.CharField(max_length=200, blank=True, null=True) 
#     choice_e =  models.CharField(max_length=200, blank=True, null=True) 
#     choice_f =  models.CharField(max_length=200, blank=True, null=True) 
    

#     mcq_answer = models.CharField(max_length=200, blank=True, null=True)  
#     mcq_answer2 = models.CharField(max_length=200, blank=True, null=True)

#     tag1 = models.CharField(max_length = 100, blank=True, null=True)
#     tag2 = models.CharField(max_length=100, blank=True, null=True)
#     tag3 = models.CharField(max_length=100, blank=True, null=True)
#     tag4 = models.CharField(max_length=100, blank=True, null=True)
#     tag5 = models.CharField(max_length=100, blank=True, null=True)

#     tag_topic = models.CharField(max_length=100, blank=True, null=True)
#     tag_sub_topic = models.CharField(max_length=100, blank=True, null=True)
#     tag_content = models.CharField(max_length=100, blank=True, null=True)

#     tag_inconsistent = models.CharField(max_length=200, blank=True, null=True)






#     explanation_text = models.TextField( blank=True, null=True)
#     explanation_image = models.ImageField(upload_to='images/mcq/', blank=True, null=True)

#     pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
#     edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)

#     uploader = models.ForeignKey(User, blank=True, null=True)


#     def update_date(self):
#         if (not self.pub_date):
#             self.pub_date = timezone.now()

#         self.edit_date = timezone.now()

#         self.save()  





#     def __unicode__(self):
#         # s = ""
#         # s = "Q: " + str(self.question_text)
#         # s += " Tag: " + str(self.tag1)
#         #return "%50s %10s %10s %10s" % (self.question_text, self.tag1, self.tag2, self.tag3)
#         # s = "{:30}  {:10} {:10}".format(self.question_text, self.tag1, self.tag2)
#         # s = "..        alamin........  qartqewrewerwrewqrrqewreqwerq34521erfdsasdfasdfdfgwe45243erafadsfq435   b"
#         s = 'Q: %s ..|||.. .t_topic:%s .t_sub_topic:%s .t_content:%s .t1:%s .t2:%s .t3:%s .t4:%s .t5:%s' % (self.question_text,
#          self.tag_topic, self.tag_sub_topic, 
#             self.tag_content, self.tag1, self.tag2, self.tag3, self.tag4, self.tag5)


#         return  s

#     class Meta:
#         verbose_name=" Individual MCQ Questions "




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

# class MarkedText(models.Model):
#     marked_text = models.CharField(max_length=100)
#     user = models.ForeignKey(User, null=True, blank=True)


#     def __unicode__(self):
#         return self.marked_text




