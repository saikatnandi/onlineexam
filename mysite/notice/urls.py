from django.conf.urls import url

from . import views
app_name = 'notice'
urlpatterns = [
    # # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<notice_id>[0-9]+)/$', views.notice_details, name='notice_details'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', views.topic_details, name='topic_details'),
    # url(r'^topic/(?P<topic_id>[0-9]+)/notice/(?P<notice_id>[0-9]+)$', views.notice_details2, name='notice_details2'),
    


    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='qadetail'),
    # # this fileupload url is for uploading image to database. This can also be uploaded through admin panel
    # url(r'^fileupload/$', views.fileupload, name= 'fileupload'),
    # # this is for parsing excel files. Through this the admin will be able to upload huge number of mcqs through excel file

    # url(r'^excelparsing/$', views.excelparsing, name= 'excelparsing'),
    # # url(r'^dashboard/$', views.dashboard, name= 'dashboard'),
    
   
]