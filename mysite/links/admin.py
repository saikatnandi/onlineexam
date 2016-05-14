from django.contrib import admin

from .models import *
from django.utils import timezone
from announcement.models import *


def getString(title):
    try:
        title = str(title)
    except Exception:
        title = title.encode('UTF8')

    # print ("\n ********** retirng strign: " + title)
    return title




def manage_notification(request, obj, form, change):
    notification = User_Notification.objects.filter(link_id = obj.id).order_by("-edit_date")
    if(notification):
        notification = notification[0]
    else:

        
        title = getString(obj.link_title)

        text = "New Link " + title + " Has Been Created/Edited"
        notification = User_Notification(notification_text = text)
        notification.link = obj        
    


    notification.update_date()
    if (not notification.uploader):
        notification.uploader = request.user        

    notification.save()        





        


   
class Link_SetInline(admin.StackedInline):
    model = Link
    extra = 0

# class Mcq_QuestionInline(admin.TabularInline):
#     model = Mcq_Question
#     extra = 0

class Link_Admin(admin.ModelAdmin):
    search_fields = ('link_title', )
    list_filter = ('pub_date', 'edit_date')
    list_display = ('link_title', 'uploader', 'pub_date', 'edit_date')

    raw_id_fields = ('link_topic', )
    exclude = ('pub_date', 'edit_date')

    # def get_queryset(self, request):
    #     qs = super(Question_Set_Admin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)


    fieldsets = [
         
         (
          'Write Title For Link ',  {'fields': ['link_title']}
          ),

         (
          'Write Details Of Link ',  {'fields': ['link_text']}
          ),


         (
          'Select Parent Category(Under Which Link Category This Link Exists) Of This Link: ', 
           {'fields': ['link_topic']}
           
          ),


          (
          'Add Video URLs For This Link: ',  {'fields': ['video_url_1', 'video_url_2', 'video_url_3']}
          ),


          (
          'Add Urls For This Link: ',  {'fields': ['link_url_1', 'link_url_2', 'link_url_3', 'link_url_4', 'link_url_5']}
          ),



          (
          'Add Images For This Link: ',  {'fields': ['image1', 'image2', 'image3']}
          ),


          (
          'Add Files For This Link: ',  {'fields': ['file1', 'file2', 'file3']}
          ),



       
    ]    

    def save_model(self, request, obj, form, change):
        
        obj.update_date()
        if (not obj.uploader):
            obj.uploader = request.user
        obj.save()
        manage_notification(request, obj, form, change)




class Link_Topic_Admin(admin.ModelAdmin):
    search_fields = ('notice_topic_text' ,)
    # inlines = [Notice_SetInline]
    
   


admin.site.register(Link, Link_Admin)

# admin.site.register(Image)
# admin.site.register(MarkedText, MarkedText_Admin)
# admin.site.register(Question_Set, Question_Set_Admin)
admin.site.register(Link_Topic, Link_Topic_Admin)

# Register your models here.
