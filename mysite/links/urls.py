from django.conf.urls import url

from . import views
app_name = 'links'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<link_id>[0-9]+)/$', views.link_details, name='link_details'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', views.topic_details, name='topic_details'),



    # # ex: /polls/
    # url(r'^$', views.index, name='index'),
    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='qadetail'),
    # # this fileupload url is for uploading image to database. This can also be uploaded through admin panel
    # url(r'^fileupload/$', views.fileupload, name= 'fileupload'),
    # # this is for parsing excel files. Through this the admin will be able to upload huge number of mcqs through excel file

    # url(r'^excelparsing/$', views.excelparsing, name= 'excelparsing'),
    # # url(r'^dashboard/$', views.dashboard, name= 'dashboard'),
    
   
]