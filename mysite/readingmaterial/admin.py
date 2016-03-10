from django.contrib import admin

# Register your models here.
from .models import *
from qa1.admin import *

from django.utils import timezone

# class Question_Set2_Admin(admin.ModelAdmin):    
#     filter_horizontal = ('mcq_question_set',)

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

    # def save_model(self, request, obj, form, change):
    #     print ("\n\n printing about obj " + str(obj))
    #     if (obj.user is None):
    #         obj.user = request.user
    #     obj.save()


class SubTopic1Inline(admin.TabularInline):
    model = SubTopic1
    extra = 0


class ReadingContentInline(admin.TabularInline):
    model = ReadingContent
    extra = 0

class SubTopic1_Admin(admin.ModelAdmin):
    search_fields = ('subtopic1_text', )

    inlines = [ReadingContentInline]

    def save_model(self, request, obj, form, change):
        print ("............saving subtopic\n\n****")       
        obj.save()

    


class ReadingContent_Admin(admin.ModelAdmin):
    # filter_horizontal = ('mcq_question', )
    list_display = ('content_title', 'uploader', 'pub_date', 'edit_date')
    list_filter = ('pub_date', 'edit_date', 'reading_topic', 'subtopic1')
    filter_horizontal = ('mcq_question', )
    raw_id_fields = ('subtopic1', )
    # inlines = [Mcq_QuestionInline]
    fieldsets = [
        
         (
          'Main Part: ',  {'fields': ['content_title', 'content_body']}
          ),

         

         (
          'Content Hierarchy: ',  {'fields': ['subtopic1', 'reading_topic']}
          ),

         (
          'Content Listed MCQ: ',  {'fields': ['mcq_question']}
          ),

         (
          'Images: ',  {'fields': ['image1', 'image2', 'image3', 'image4', 'image5']}
          ),


        
    ]  

    def save_model(self, request, obj, form, change):
        print ("............saving content\n\n****")
    	
        # print (rt)

        if (not obj.pub_date):
            obj.pub_date = timezone.now()

        obj.edit_date = timezone.now()


        if (obj.subtopic1):
    		# if ((obj.reading_topic)):
           if (True):
                print ("obj.subtopic1: " + str(obj.subtopic1))
                rt = ReadingTopic.objects.get(subtopic1=(obj.subtopic1))
                obj.reading_topic = rt

                print ("\n\n\n i need to upadte the reading topic \n\n")
                print (rt)

        obj.save()

        if (obj.mcq_question):
            print ('trying to update the tag_content of mcq of this reading content: ' )
            mcq = Mcq_Question.objects.filter(readingcontent__id = obj.id)
            # print ("these mcqs tag_content will be updated: \n")
            # print (mcq)

            # print ("other obj's mcq: ")
            # print (obj.mcq_question)

            for m in mcq:
                m.tag_content = obj.content_title
                m.tag_sub_topic = str(obj.subtopic1)
                m.tag_topic = str(obj.reading_topic)
                if (not m.pub_date):
                    m.pub_date = timezone.now()
                m.edit_date = timezone.now()
                m.save()
        


        mcq = Mcq_Question.objects.filter(tag_content=obj.content_title).exclude(readingcontent__id = obj.id)
        for m in mcq:
            m.tag_content = None
            if (not m.pub_date):
                m.pub_date = timezone.now()
            m.edit_date = timezone.now()
            m.save()
        # print ("these mcqs tag_content will be removed: ")
        # print (mcq)

        mcq = Mcq_Question.objects.filter(readingcontent__id__in = ReadingContent.objects.all())        

        seen = set()
        # uniq = []
        duplicate = []
        for x in mcq:
            if x in seen:
                # uniq.append(x)
                duplicate.append(x)

            else:
                seen.add(x)

        for m in duplicate:
            print ("*******in for duplicate loop")


            reading_content = ReadingContent.objects.filter(mcq_question=m).exclude(content_title = obj.content_title)

            # print ('**********The inconsistent tag is: ' + str(reading_content))
            m.tag_inconsistent = str(reading_content[0].content_title)
            if (not m.pub_date):
                m.pub_date = timezone.now()
            m.edit_date = timezone.now()
            m.save()

        print ("\n\n\n *********trying to find out inconsistent mcq: \n\n")
        print (duplicate)
         

        print ("over")




        # print ("\n\n in readin content admin page  " + str(obj))
        # if (obj.mcq_question is None):
        #     print ("mcq .........NOT have any.... content tag")
        # #     obj.user = request.use
        # else:

        #     print ("mcq already has a content tag")
        #     print (obj.mcq_question.tag1)

        # print (obj.mcq_question)
        



class ReadingTopic_Admin(admin.ModelAdmin):
	inlines = [SubTopic1Inline]


admin.site.register(ReadingTopic, ReadingTopic_Admin)
admin.site.register(SubTopic1, SubTopic1_Admin)
# admin.site.register(SubTopic2)
admin.site.register(ReadingContent, ReadingContent_Admin)


admin.site.register(ContentNotes)
admin.site.register(ContentMarkedText)
admin.site.register(ContentMarkedMcq)
admin.site.register(ContentComment)