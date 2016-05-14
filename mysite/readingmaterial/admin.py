from django.contrib import admin

# Register your models here.
from .models import *
from qa1.admin import *

from django.utils import timezone
from announcement.models import *

def DoFunc(modeladmin, request, queryset):
    print ("***** in update publish time method ***")
    for obj in queryset:
        obj.tid = obj.reading_topic_id
        obj.stid = obj.subtopic1_id
        obj.save()







class SubTopic1Inline(admin.TabularInline):
    model = SubTopic1
    extra = 0


class ReadingContentInline(admin.TabularInline):
    model = ReadingContent
    extra = 0

class ReadingTopic_Admin(admin.ModelAdmin):
    search_fields = ('reading_topic_text', )
    list_display = ('id', 'reading_topic_text',)
    # list_filter = ('reading_topic_text',)


    inlines = [SubTopic1Inline]


class ContentNotes_Admin(admin.ModelAdmin):
    search_fields = ('content_notes', )
    list_display = ('id', 'content_notes', 'user', 'content')
    # list_filter = ('reading_topic_text',)


    # inlines = [SubTopic1Inline]





class SubTopic1_Admin(admin.ModelAdmin):
    search_fields = ('subtopic1_text', )
    list_display = ('id', 'subtopic1_text', 'topic', 'tid')
    list_filter = ('topic',)

    raw_id_fields = ('topic', )
    exclude = ('tid', )


    inlines = [ReadingContentInline]

    def save_model(self, request, obj, form, change):
        print ("............saving subtopic\n\n****")       
        obj.tid = obj.topic_id
        obj.save()

    
def manage_notification(obj, request, form, change):
    notification = User_Notification.objects.filter(reading_content_id = obj.id).order_by("-edit_date")
    if(notification):
        notification = notification[0]
    else:


        try:
            title = str(obj.content_title)
        except Exception:
            title = obj.content_title.encode('utf8')


        text = "New Reading Content " + title + " Has Been Created/Edited"
        notification = User_Notification(notification_text = text)
        notification.reading_content = obj        
    


    notification.update_date()
    if (not notification.uploader):
        notification.uploader = request.user        

    notification.save()






class ReadingContent_Admin(admin.ModelAdmin):
    # filter_horizontal = ('mcq_question', )
    list_display = ('id', 'content_title','reading_topic' , 'tid', 'subtopic1', 'stid', 'uploader' , 'pub_date', 'edit_date')
    list_filter = ('pub_date', 'edit_date', 'reading_topic', 'subtopic1')
    # filter_horizontal = ('mcq_question', )
    raw_id_fields = ('subtopic1', 'reading_topic', )
    search_fields = ('content_title' ,)
    # inlines = [Mcq_QuestionInline]

    actions = [DoFunc]

    fieldsets = [

         (
          'Content Hierarchy: ',  {'fields': ['subtopic1']}
          ),

         (
          'Content Hierarchy(Topic) (If You Have Selected Sub Topic Then Skip) ',  {'fields': [ 'reading_topic']}
          ),

         (
          'Main Part: ',  {'fields': ['content_title', 'content_body']}
          ),

         


         # (
         #  'Content Listed MCQ: ',  {'fields': ['mcq_question']}
         #  ),

         (
          'Images: ',  {'fields': ['image1', 'image2', 'image3', 'image4', 'image5']}
          ),


        
    ]  

    def save_model(self, request, obj, form, change):
        print ("............saving content\n\n****")
        
        # print (rt)
        obj.update_date()
        if (not obj.uploader):
            obj.uploader = request.user
        obj.save() 

        if ( obj.subtopic1):
            topic = obj.subtopic1.topic
            obj.reading_topic = topic
            

        obj.tid = obj.reading_topic_id
        obj.stid = obj.subtopic1_id
        obj.save()


        manage_notification( obj, request, form, change)


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
        


        


class Quick_Question_Admin(admin.ModelAdmin):
    search_fields = ('quick_question_text', )
    list_filter = ('pub_date', 'edit_date')
    list_display = ('id','quick_question_text', 'uploader', 'content', 'pub_date', 'edit_date')

    raw_id_fields = ('content', )
    exclude = ('pub_date', 'edit_date')

    # def get_queryset(self, request):
    #     qs = super(Question_Set_Admin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)


    fieldsets = [
         
         (
          'Write Quick Question ',  {'fields': ['quick_question_text']}
          ),

         (
          'Write Answer ',  {'fields': ['quick_question_answer']}
          ),

          (
          'Reading Content Id ',  {'fields': ['content']}
          ),



       
    ]    

    def save_model(self, request, obj, form, change):
        
        obj.update_date()
        if (not obj.uploader):
            obj.uploader = request.user
        obj.save()












admin.site.register(ReadingTopic, ReadingTopic_Admin)
admin.site.register(SubTopic1, SubTopic1_Admin)
# admin.site.register(SubTopic2)
admin.site.register(ReadingContent, ReadingContent_Admin)
admin.site.register(Quick_Question, Quick_Question_Admin)

admin.site.register(ContentNotes, ContentNotes_Admin)
admin.site.register(ContentMarkedText)
# admin.site.register(ContentMarkedMcq)
admin.site.register(ContentComment)
admin.site.register(Marked_Quick_Question)
admin.site.register(Finished_Content)