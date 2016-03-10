from django.contrib import admin

from .models import *
from django.utils import timezone


from question.models import *


def Update_published_time(modeladmin, request, queryset):
    print ("***** in update publish time method ***")
    for obj in queryset:
        obj.update_date()


def Update_Uploader_Information(modeladmin, request, queryset):
    print ("***** in update publish time method ***")

    if (request.user.is_superuser):      
      for obj in queryset:
          obj.uploader = request.user
          obj.save()



        
class Mcq_Question_Admin(admin.ModelAdmin):
    list_display = ('question_text', 'uploader', 'tag5', 'tag_content', 'mcq_answer','pub_date', 'edit_date')
    list_filter = ( 'pub_date', 'edit_date','tag_topic', 'tag_sub_topic', 
                   'tag_content','tag1','tag2','tag3', 'tag4', 'tag5' )
#    search_fields = ('tag_set__tag_text','question_text')
    search_fields = ( 'tag_topic', 'tag_sub_topic', 'tag_content','question_text',
                    'tag1', 'tag2', 'tag3', 'tag4', 'tag5')

    actions = [Update_published_time, Update_Uploader_Information]



    # filter_horizontal = ('tag_set',)
    # exclude = ('pub_date', )

    fieldsets = [
         (
          'MCQ Question: ',  {'fields': ['question_text',
          'choice_a', 'choice_b', 'choice_c', 'choice_d']}
          ),

         (
          'MCQ Question Image: ',  {'fields': ['mcq_image']}
          ),


         (
          'MCQ Optional Fields (In Case There Is More Than One Choices For A Question). Leave Blank If Not Necessary: ', 
           {'fields': [ 'choice_e', 'choice_f']}
          ),

         (
          'MCQ Answer: ',  {'fields': ['mcq_answer', 'mcq_answer2']}
          ),

         (
          'MCQ  Tag: ',  {'fields': ['tag1', 'tag2', 'tag3', 'tag4', 

          'tag5', 'tag_topic','tag_sub_topic', 'tag_content']}
          ),

        
        ('MCQ Explanation: ', {'fields': ['explanation_text', 'explanation_image']}),
        # ('Others: ', {'fields': ['pub_date']}),
    ]

    def get_queryset(self, request):
        qs = super(Mcq_Question_Admin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(uploader=request.user)

    def save_model(self, request, obj, form, change):
        print ("\n\n printing about obj " + str(obj))
        obj.update_date()
        if (not obj.uploader):
            obj.uploader = request.user
        obj.save()
        # if (not obj.pub_date):
        #     obj.pub_date = timezone.now()

        # obj.edit_date = timezone.now()
        # obj.save()


# class Mcq_Question_Admin(admin.ModelAdmin):
#     list_display = ('question_text', 'mcq_answer')
#     list_filter = ('tag1','tag2','tag3',)
# #    search_fields = ('tag_set__tag_text','question_text')
#     search_fields = ('tag1','question_text')
#     filter_horizontal = ('tag_set',)

class Question_Set2_Admin(admin.ModelAdmin):    
    filter_horizontal = ('mcq_question_set',)

class MarkedText_Admin(admin.ModelAdmin):
    list_display = ('user', 'marked_text')
    list_filter = ('user',)
    def get_queryset(self, request):
        qs = super(MarkedText_Admin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        print ("\n\n printing about obj " + str(obj))
        if (obj.user is None):
            obj.user = request.user
        obj.save()
   
class Question_SetInline(admin.StackedInline):
    model = Question_Set
    extra = 0

# class Mcq_QuestionInline(admin.TabularInline):
#     model = Mcq_Question
#     extra = 0

class Question_Set_Admin(admin.ModelAdmin):
    search_fields = ('question_set_text', )
    list_filter = ('pub_date', 'edit_date')
    list_display = ('question_set_text', 'uploader', 'pub_date', 'edit_date')
    filter_horizontal = ('mcq_question',)
    raw_id_fields = ('question_topic', )
    exclude = ('pub_date', 'edit_date')

    # def get_queryset(self, request):
    #     qs = super(Question_Set_Admin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)


    fieldsets = [
         
         (
          'Write Title For This Question Set ',  {'fields': ['question_set_text']}
          ),


         (
          'Select Parent Category(Under Which Question Category This Question Set Exists) Of This Question Set: ', 
           {'fields': ['question_topic']}
          ),

          (
          'Question Setting: ',  {'fields': ['individual_mcq_marks', 'negative_marking_percentage']}
          ),

         (
          'Select MCQ For This Question Set: ',  {'fields': ['mcq_question']}
          ),


       
    ]    

    def save_model(self, request, obj, form, change):
        # print ("\n\n printing about obj " + str(obj))
        if (not obj.pub_date):
            obj.pub_date = timezone.now()

        obj.edit_date = timezone.now()
        obj.save()





class Question_Topic_Admin(admin.ModelAdmin):
    search_fields = ('question_topic_text' ,)
    inlines = [Question_SetInline]
    
   


admin.site.register(Mcq_Question, Mcq_Question_Admin)
# admin.site.register(Topic)
# admin.site.register(Question_Set)
# admin.site.register(Tag)
# admin.site.register(Subject)
# admin.site.register(Question_Set2, Question_Set2_Admin)
# admin.site.register(Image)
admin.site.register(MarkedText, MarkedText_Admin)
admin.site.register(Question_Set, Question_Set_Admin)
admin.site.register(Question_Topic, Question_Topic_Admin)

# Register your models here.
