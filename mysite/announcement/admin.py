from django.contrib import admin

from .models import *
from django.utils import timezone



        


   




class Announcement_Admin(admin.ModelAdmin):
    search_fields = ('announcement_text', )
    list_filter = ('pub_date', 'edit_date')
    list_display = ('announcement_text', 'uploader', 'start_date', 'end_date','url')


    exclude = ('pub_date', 'edit_date')

    # def get_queryset(self, request):
    #     qs = super(Question_Set_Admin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)


    fieldsets = [
         
         (
          'Write Your Important Announcement',  {'fields': ['announcement_text']}
          ),

         (
          'Write The URL  ',  {'fields': ['url']}
          ),




          (
          'Add Date Information ',  {'fields': ['start_date', 'end_date']}
          ),




       
    ]    

    def save_model(self, request, obj, form, change):
        
        obj.update_date()
        if (not obj.uploader):
            obj.uploader = request.user
        obj.save()




class User_Notification_Admin(admin.ModelAdmin):
    search_fields = ('notification_text', )
    list_filter = ('pub_date', 'edit_date')
    list_display = ('notification_text', 'pub_date', 'edit_date', 'uploader',
     'url','notice', 'link', 'question_set', 'reading_content')

    raw_id_fields = ('notice', 'link', 'question_set', 'reading_content',)


    exclude = ('pub_date', 'edit_date')

    # def get_queryset(self, request):
    #     qs = super(Question_Set_Admin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)


    fieldsets = [
         
         (
          'Write Your Notification',  {'fields': ['notification_text']}
          ),

         (
          'Write The URL  ',  {'fields': ['url']}
          ),


         (
          'Notification For Following Content  ',  {'fields': ['notice', 'link', 'question_set', 'reading_content']}
          ),


          # (
          # 'Add Date Information ',  {'fields': ['start_date', 'end_date']}
          # ),




       
    ]    

    def save_model(self, request, obj, form, change):
        
        obj.update_date()
        if (not obj.uploader):
            obj.uploader = request.user
        obj.save()














admin.site.register(Announcement, Announcement_Admin)
admin.site.register(User_Notification, User_Notification_Admin)

