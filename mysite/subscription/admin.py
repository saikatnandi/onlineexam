from django.contrib import admin

from .models import *
from django.utils import timezone
from question.models import *






class Subscription_Plan_Admin(admin.ModelAdmin):
    search_fields = ('subscription_plan_title', )
 
    list_display = ('subscription_plan_title', 'subscription_fee', 
    	'subscription_duration', 
      
      'no_of_exam_per_day',
    	'no_of_random_question',
      'can_create_blog_tag',
      'bkash_no',
      )

    # raw_id_fields = ('notice_topic', )
    # exclude = ('pub_date', 'edit_date')

    # def get_queryset(self, request):
    #     qs = super(Question_Set_Admin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)


    fieldsets = [
         
         (
          'Write Plan Name ',  {'fields': ['subscription_plan_title']}
          ),

         (
          'Subscription Fee ',  {'fields': ['subscription_fee']}
          ),

        (
          'Bkash No (Money Send To This Number) ',  {'fields': ['bkash_no']}
          ),

         (
          'Subscription Duration(In Days)(-1 Value Means Unlimited)  ', 
           {'fields': ['subscription_duration']}
          ),



          (
          'Can This User Create Blog Tag ',  {'fields': ['can_create_blog_tag']}
          ),


          (
     'Enter Total No Of Exam This Plan Supports Per Day (-1 Value Means Unlimited) ', 
      {'fields': ['no_of_exam_per_day']}
          ),   


          (
     'Enter Total No Of Random Question This Plan Supports (-1 Means Unlimited) ', 
      {'fields': ['no_of_random_question']}
          ),



       
    ]    

    def save_model(self, request, obj, form, change):
    	obj.save()
        





# class Special_Plan_Admin(admin.ModelAdmin):
#     search_fields = ('special_plan_title', )
 
#     list_display = ('special_plan_title', 'special_plan_fee', 

#       'bkash_no',
#       )




#     fieldsets = [
         
#          (
#           'Write Plan Name ',  {'fields': ['special_plan_title']}
#           ),

#          (
#           'Subscription Fee ',  {'fields': ['special_plan_fee']}
#           ),

#         (
#           'Bkash No (Money Send To This Number) ',  {'fields': ['bkash_no']}
#           ),





       
#     ]    

#     def save_model(self, request, obj, form, change):
#       obj.save()
        

















class Subscription_Admin(admin.ModelAdmin):
    search_fields = ('token', )
    list_filter = ('is_valid',)
    raw_id_fields = ('user', 'subscription_plan' )    
 
    list_display = ('subscription_plan', 'user', 
      # 'is_confirmed',
      'is_valid', 
      'no_of_exam_per_day',
      'no_of_random_question',

      'start_date', 
      'end_date',

      

      )

    # raw_id_fields = ('notice_topic', )
    # exclude = ('pub_date', 'edit_date')

    # def get_queryset(self, request):
    #     qs = super(Question_Set_Admin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)


    fieldsets = [
         
         (
          'Select Plan And User ',  {'fields': ['user','subscription_plan']}
          ),

         # (
         #  'Is Subscription Accepted (Is Payment Completed?) ',  {'fields': ['is_confirmed']}
         #  ),




         (
          'Date Information(Keep Blank And They will Be Auto Filled)  ', 
           {'fields': [
           # 'request_date', 
           'start_date', 
            'end_date'
            ]}
          ),



          (
     'Enter Total No Of Exam This Plan Supports Per Day (-1 Value Means Unlimited) ', 
      {'fields': ['no_of_exam_per_day']}
          ),   


          (
     'Enter Total No Of Random Question This Plan Supports (-1 Means Unlimited) ', 
      {'fields': ['no_of_random_question']}
          ),


         (
          'Is Subscription Valid (Is Period Expired?) ',  {'fields': ['is_valid']}
          ),




       
    ]    

    # def save_model(self, request, obj, form, change):
    #     if (not obj.request_date):
    #         obj.request_date = timezone.now()
    #     flag = True

    #     print ("\n\n**************** in subscription save method")
    #     if (obj.is_confirmed):

    #         if ((not obj.start_date) and (not obj.end_date)):
    #             subscription = Subscription.objects.filter(user=obj.user, 
    #              subscription_plan=obj.subscription_plan, is_confirmed=True, is_valid=True)
    #             print (subscription)
    #             print ("****** ******* check if going to save")
    #             if (subscription):
    #                 # print ("\n\n****** ******* not going to save")                   
    #                 subscription = subscription[0]
    #                 day = obj.subscription_plan.subscription_duration
    #                 subscription.end_date = subscription.end_date + timezone.timedelta(days=day)
    #                 subscription.save()
    #                 flag = False
    #                 obj.start_date = timezone.now()
    #                 obj.save()

    #         #         print ("value of flag: " )
    #         #         print (flag)

    #         # print ("value of flag: " )
    #         # print (flag)
    #         if (flag):
    #             print ("***** if flag ")            
    #             if (not obj.start_date):
    #                 obj.start_date = timezone.now()

    #               # obj.is_valid = True

    #             day = obj.subscription_plan.subscription_duration
    #             if (not obj.end_date):
    #                 obj.end_date = timezone.now() + timezone.timedelta(days=day)

    #             obj.save()

    #             if (obj.end_date > timezone.now()):
    #                 obj.is_valid = True


        
    #     if (flag):
    #         obj.save()
    #         obj.update_validity()
            





class Subscription_Request_Admin(admin.ModelAdmin):
    search_fields = ('token', 'user')
    list_filter = ('is_confirmed','is_valid')
    raw_id_fields = ('user', 'subscription_plan' )    
 
    list_display = ('subscription_plan', 'user', 'token', 
      'is_confirmed',
      'is_valid', 

      'request_date',       

      )




    fieldsets = [
      


         (
          'Is Subscription Accepted (Is Payment Completed?) ',  {'fields': ['is_confirmed']}
          ),

         (
          'Select Plan And User ',  {'fields': ['user','subscription_plan']}
          ),




         (
          'Date Information(Keep Blank And They will Be Auto Filled)  ', 
           {'fields': [
           'request_date', 

            ]}
          ),



         # (
         #  'Is Subscription Valid (Has This Request Been Processed?)(This Field Will ) ',  {'fields': ['is_valid']}
         #  ),




       
    ]    




    def save_model(self, request, obj, form, change):
        if (not obj.request_date):
            obj.request_date = timezone.now()
        flag = True

        print ("\n\n**************** in subscription save method")
        if (obj.is_valid):
            if (obj.is_confirmed):
                subscription = Subscription.objects.filter(user=obj.user, 
                               subscription_plan=obj.subscription_plan,
                                is_valid=True).order_by("-id")

                print (subscription)
                print ("****** ******* check if going to save")
                if (subscription):
                    # print ("\n\n****** ******* not going to save")                   
                    subscription = subscription[0]
                    day = obj.subscription_plan.subscription_duration
                    subscription.end_date = subscription.end_date + timezone.timedelta(days=day)

                    print (obj.subscription_plan.no_of_exam_per_day)
                    if (obj.subscription_plan.no_of_exam_per_day != -1):
                        print ("********* in exam per day condition")
                        subscription.no_of_exam_per_day = subscription.no_of_exam_per_day + obj.subscription_plan.no_of_exam_per_day

                    if (obj.subscription_plan.no_of_random_question != -1):
                        subscription.no_of_random_question = subscription.no_of_random_question + obj.subscription_plan.no_of_random_question



                    subscription.save()
                    # flag = False
                    # obj.start_date = timezone.now()
                    # obj.save()

                else:
                    subscription = Subscription(user=obj.user)
                    # plan = Subscription_Plan.objects.get(id = plan_id)
                    subscription.subscription_plan = obj.subscription_plan
                    subscription.start_date = timezone.now()

                    day = obj.subscription_plan.subscription_duration

                    subscription.end_date = timezone.now() + timezone.timedelta(days=day) 
                    # subscription.save()
                    subscription.is_valid = True
                    subscription.no_of_random_question = obj.subscription_plan.no_of_random_question
                    subscription.no_of_exam_per_day = obj.subscription_plan.no_of_exam_per_day
                    subscription.save()

                obj.is_valid = False





            #         print ("value of flag: " )
            #         print (flag)

            # print ("value of flag: " )
            # print (flag)
        

        obj.save()
        obj.update_validity()

        #     if (flag):
        #         print ("***** if flag ")            
        #         if (not obj.start_date):
        #             obj.start_date = timezone.now()

        #           # obj.is_valid = True

        #         day = obj.subscription_plan.subscription_duration
        #         if (not obj.end_date):
        #             obj.end_date = timezone.now() + timezone.timedelta(days=day)

        #         obj.save()

        #         if (obj.end_date > timezone.now()):
        #             obj.is_valid = True


        
        # if (flag):
        #     obj.save()
        #     obj.update_validity()
            














# class Subscription_Special_Plan_Admin(admin.ModelAdmin):
#     search_fields = ('token', )
#     list_filter = ('is_confirmed',)
#     raw_id_fields = ('user', 'special_plan' )    
 
#     list_display = ('special_plan', 'user', 'token', 



#       'request_date', 

#       'is_confirmed',
      

#       )




#     fieldsets = [
         
#          (
#           'Select Plan And User ',  {'fields': ['user','special_plan']}
#           ),

#          (
#           'Is Subscription Accepted (Is Payment Completed?) ',  {'fields': ['is_confirmed']}
#           ),




#          (
#           'Date Information(Keep Blank And They will Be Auto Filled)  ', 
#            {'fields': [
#            'request_date', 

#             ]}
#           ),









       
#     ]    

#     def save_model(self, request, obj, form, change):
#         if (not obj.request_date):
#             obj.request_date = timezone.now()

        
#         obj.save()
          













# class Notice_Topic_Admin(admin.ModelAdmin):
#     search_fields = ('notice_topic_text' ,)
#     # inlines = [Notice_SetInline]
    
   


admin.site.register(Subscription_Plan, Subscription_Plan_Admin)
# admin.site.register(Special_Plan, Special_Plan_Admin)


admin.site.register(Subscription, Subscription_Admin)
admin.site.register(Subscription_Request, Subscription_Request_Admin)
# admin.site.register(Subscription_Special_Plan, Subscription_Special_Plan_Admin)



# admin.site.register(Notice_Topic, Notice_Topic_Admin)

