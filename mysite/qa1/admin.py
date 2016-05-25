from django.contrib import admin

from .models import *
from django.utils import timezone


from question.models import *
from announcement.models import *

def getString(title):
    try:
        title = str(title)
    except Exception:
        title = title.encode('UTF8')

    # print ("\n ********** retirng strign: " + title)
    return title


def Update_published_time(modeladmin, request, queryset):
    print ("***** in update publish time method ***")
    for obj in queryset:
        obj.update_date()


def Fix_Problem_None_Of_choice_ef(modeladmin, request, queryset):
    print ("***** iFix_Problem_None_Of_choice_ef  ***")
    for obj in queryset:

        if (getString(obj.choice_f) == "None"):
            # print ("*** going to update choice_ef")
            obj.choice_e=""
            obj.choice_f=""
            obj.save()




def Update_Uploader_Information(modeladmin, request, queryset):
    print ("***** in update publish time method ***")

    if (request.user.is_superuser):      
      for obj in queryset:
          obj.uploader = request.user
          obj.save()



def DoSomeTask(modeladmin, request, queryset):
    print ("***** in update publish time method ***")
    for obj in queryset:
        obj.update_date()



        
class Mcq_Question_Admin(admin.ModelAdmin):
    list_display = ('id','question_text', 'uploader', 'tag5', 'tag_content', 'mcq_answer','pub_date', 'edit_date')
    list_filter = ( 'pub_date', 'edit_date','tag_topic', 'tag_sub_topic', 
                   'tag_content','tag1','tag2','tag3', 'tag4', 'tag5' )
#    search_fields = ('tag_set__tag_text','question_text')
    search_fields = ( 'id', 'tag_topic', 'tag_sub_topic', 'tag_content','question_text',
                    'tag1', 'tag2', 'tag3', 'tag4', 'tag5')

    raw_id_fields = ('subtopic1', 'reading_topic', )    

    actions = [Update_published_time, Update_Uploader_Information, Fix_Problem_None_Of_choice_ef]



    # filter_horizontal = ('tag_set',)
    # exclude = ('pub_date', )

    fieldsets = [

         (
          'MCQ Topic(If You Select SubTopic Then Skip): ',  
          {'fields': ['reading_topic']}
          ),

         (
          'MCQ Sub Topic',  
          {'fields': ['subtopic1']}
          ),
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



def manage_notification(request, obj, form, change):
    notification = User_Notification.objects.filter(question_set_id = obj.id).order_by("-edit_date")
    if(notification):
        notification = notification[0]
    else:

        try:
            title = str(obj.question_set_text)
        except Exception:
            title = obj.question_set_text.encode('utf8')


        text = "New Question Set " + title + " Has Been Created/Edited"
        notification = User_Notification(notification_text = text)
        notification.question_set = obj        
    


    notification.update_date()
    if (not notification.uploader):
        notification.uploader = request.user        

    notification.save()




class Question_Set_Admin(admin.ModelAdmin):
    search_fields = ('question_set_text', )
    list_filter = ('pub_date', 'edit_date', 'is_free',)
    list_display = ('id','question_set_text', 'uploader', 'is_free','pub_date', 'edit_date')
    filter_horizontal = ('mcq_question', 'subscription_plan', 'reading_content')
    raw_id_fields = ('question_topic', 'subtopic1', 'reading_topic', )
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
          '(If It Is A Topic Wise Test)Select Parent Category(Under Which Question Category This Question Set Exists) Of This Question Set: ', 
           {'fields': [ 'subtopic1', 'reading_topic', 'reading_content']}
          ),

          (
          'Question Setting: ',  {'fields': ['individual_mcq_marks', 'negative_marking_percentage', 'individual_mcq_time']}
          ),

          (
          'Is This Question Set Free: ',  {'fields': ['is_free',]}
          ),


         (
          'IF Question Set Not Free Then Choose Subscription Plan Users Who Will Be Able To Enjoy It Free: ',
            {'fields': ['subscription_plan']}
          ),

         # (
         #  'IF Question Set Not Free Then Choose Special  Plan Users Who Will Be Able To Enjoy It Free: ',
         #    {'fields': ['special_plan']}
         #  ),



         (
          'Select MCQ For This Question Set: ',  {'fields': ['mcq_question']}
          ),


       
    ]    

    def save_model(self, request, obj, form, change):
        # print ("\n\n printing about obj " + str(obj))
        obj.update_date()
        print("********going to add uploader info")
        if (not obj.uploader):
            print("********if loop of  uploader info")
            obj.uploader = request.user
        obj.save()

        # print ("\n\n\n****** a question set is either created or edited\n\n\n")
      
        manage_notification(request, obj, form, change)

        # notification = User_Notification.objects.filter(question_set_id = obj.id).order_by("-edit_date")
        # if(notification):
        #     notification = notification[0]
        # else:
        #     text = "New Question Set " + str(obj.question_set_text) + " Has Been Created/Edited"
        #     notification = User_Notification(notification_text = text)
        #     notification.question_set = obj        
        


        # notification.update_date()
        # if (not notification.uploader):
        #     notification.uploader = request.user        

        # notification.save()






class Question_Topic_Admin(admin.ModelAdmin):
    search_fields = ('question_topic_text' ,)
    list_display = ('id', 'question_topic_text',)
    inlines = [Question_SetInline]
    

class Question_Set_Result_Admin(admin.ModelAdmin):
    # search_fields = ('user', )
    list_display = ('id', 'user', 'question_set', 'marks', 'start_date', 'finish_date',)
    list_filter = (  'question_set', 'start_date', 'finish_date',)
    
class Marked_Mcq_Admin(admin.ModelAdmin):
    # search_fields = ('user', )
    list_display = ('id', 'user', 'mcq_question')
    # list_filter = (  'question_set', 'start_date', 'finish_date',)
    raw_id_fields = ('user', 'mcq_question', )
  


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
admin.site.register(Question_Set_Result, Question_Set_Result_Admin)
admin.site.register(Marked_Mcq,Marked_Mcq_Admin)


# Register your models here.
