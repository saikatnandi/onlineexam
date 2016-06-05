from django.contrib import admin

from .models import *
from django.utils import timezone



        


   




class Message_Admin(admin.ModelAdmin):
    search_fields = ('message_text', 'user', )
    list_filter = ('pub_date', 'edit_date')
    list_display = ('user', 'message_text', 'pub_date', 'edit_date',)
    raw_id_fields = ('user', )


    exclude = ('pub_date', 'edit_date')

    # def get_queryset(self, request):
    #     qs = super(Question_Set_Admin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)


    fieldsets = [
         
         (
          'Write Your Message For User',  {'fields': ['message_text']}
          ),

         (
          'Select User To Whom This Message Will Be Sent',  {'fields': ['user']}
          ),




          # (
          # 'Add Date Information ',  {'fields': ['start_date', 'end_date']}
          # ),




       
    ]    

    def save_model(self, request, obj, form, change):
        
        obj.update_date()
        # if (not obj.uploader):
        #     obj.uploader = request.user
        obj.save()




class Report_Quick_Question_Admin(admin.ModelAdmin):
    search_fields = ('report_text', )
    list_filter = ('pub_date', 'edit_date','quick_question')
    list_display = ( 'user','report_text', 'pub_date', 'edit_date',
     'quick_question')

    raw_id_fields = ('user', 'quick_question', )


    exclude = ('pub_date', 'edit_date')


    def save_model(self, request, obj, form, change):
        
        obj.update_date()
        obj.save()


class Report_Mcq_Question_Admin(admin.ModelAdmin):
    search_fields = ('report_text', )
    list_filter = ('pub_date', 'edit_date','mcq_question')
    list_display = ( 'user','report_text', 'pub_date', 'edit_date',
     'mcq_question', )

    raw_id_fields = ('user', 'mcq_question', )


    exclude = ('pub_date', 'edit_date')


    def save_model(self, request, obj, form, change):
        
        obj.update_date()
        obj.save()




admin.site.register(Message, Message_Admin)
admin.site.register(Report_Mcq_Question, Report_Mcq_Question_Admin)
admin.site.register(Report_Quick_Question, Report_Quick_Question_Admin)


