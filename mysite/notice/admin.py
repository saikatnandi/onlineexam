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




def manage_notification(request, obj, form, change):
    notification = User_Notification.objects.filter(notice_id = obj.id).order_by("-edit_date")
    if(notification):
        notification = notification[0]
    else:

        
        title = getString(obj.notice_title)

        text = "New Notice " + title + " Has Been Created/Edited"
        notification = User_Notification(notification_text = text)
        notification.notice = obj        
    


    notification.update_date()
    if (not notification.uploader):
        notification.uploader = request.user        

    notification.save()        









   
class Notice_SetInline(admin.StackedInline):
    model = Notice
    extra = 0

# class Mcq_QuestionInline(admin.TabularInline):
#     model = Mcq_Question
#     extra = 0

class Notice_Admin(admin.ModelAdmin):
    search_fields = ('notice_title', )
    list_filter = ('pub_date', 'edit_date')
    list_display = ('notice_title', 'uploader', 'pub_date', 'edit_date')

    raw_id_fields = ('notice_topic', )
    exclude = ('pub_date', 'edit_date')

    # def get_queryset(self, request):
    #     qs = super(Question_Set_Admin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)


    fieldsets = [
         
         (
          'Write Title For Notice ',  {'fields': ['notice_title']}
          ),

         (
          'Write Details Of Notice ',  {'fields': ['notice_text']}
          ),


         (
          'Select Parent Category(Under Which Notice Category This Notice Exists) Of This Notice: ', 
           {'fields': ['notice_topic']}
          ),



          (
          'Add Images For This Notice: ',  {'fields': ['image1', 'image2', 'image3']}
          ),


          (
          'Add Files For This Notice: ',  {'fields': ['file1', 'file2', 'file3']}
          ),



       
    ]    

    def save_model(self, request, obj, form, change):
        
        obj.update_date()
        if (not obj.uploader):
            obj.uploader = request.user
        obj.save()
        manage_notification(request, obj, form, change)




class Notice_Topic_Admin(admin.ModelAdmin):
    search_fields = ('notice_topic_text' ,)
    # inlines = [Notice_SetInline]
    
   


admin.site.register(Notice, Notice_Admin)

# admin.site.register(Image)
# admin.site.register(MarkedText, MarkedText_Admin)
# admin.site.register(Question_Set, Question_Set_Admin)
admin.site.register(Notice_Topic, Notice_Topic_Admin)

# Register your models here.
