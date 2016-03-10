from django.conf.urls import url

from . import views
app_name = 'question'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_topic_id>[0-9]+)/questionset/$', 
        views.question_set, name='question_set'),
    url(r'^(?P<question_topic_id>[0-9]+)/questionset/(?P<question_set_id>[0-9]+)/question/$', 
        views.question, name='question'),

    url(r'^(?P<question_topic_id>[0-9]+)/questionset/(?P<question_set_id>[0-9]+)/question/result/$', 
        views.result, name='result'),

    url(r'^automated/questionset/(?P<question_set_id>[0-9]+)/question/$', 
    views.result, name='automated_question'),

    url(r'^create/question/topicwise/$', views.create_question_topic_wise, name='create_question_topic_wise'),
    url(r'^create/question/sub/topicwise/$', views.create_question_sub_topic_wise, name='create_question_sub_topic_wise'),
    url(r'^excelparsing/$', views.excelparsing, name= 'excelparsing'),
    url(r'^excelparsing/questionset/$', views.excelparsing_question_set, name= 'excelparsing_question_set'),
    
    
    
    


    

  
    # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='qadetail'),
    # # this fileupload url is for uploading image to database. This can also be uploaded through admin panel
    # url(r'^fileupload/$', views.fileupload, name= 'fileupload'),
    # # this is for parsing excel files. Through this the admin will be able to upload huge number of mcqs through excel file

    # url(r'^excelparsing/$', views.excelparsing, name= 'excelparsing'),
    # url(r'^dashboard/$', views.dashboard, name= 'dashboard'),
    
   
]

  # url(r'^(?P<topic_id>[0-9]+)/$', views.subtopic1, name='subtopic1'),
  # 