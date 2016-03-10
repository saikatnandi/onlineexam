from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls
from django.conf.urls import include, url

from . import views
app_name = 'blog'

urlpatterns = [

    # ex: /polls/
    #url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^allpost/$', views.allpost, name='allpost'),
    url(r'^taglist/$', views.taglist, name='taglist'),
    url(r'^taglist/tagid/(?P<tag_id>[0-9]+)/allpost/$', views.allpost_by_taglist, name='allpost_by_taglist'),
 
   
    url(r'^writepost/$', views.writepost, name='writepost'),
    url(r'^allpost/(?P<post_id>[0-9]+)/$', views.post_details, name='post_details'),
    url(r'^ajax/addcomment/$', views.ajax_comment, name='ajax_comment'),


       # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # url(r'^(?P<question_set_id>[0-9]+)/startexam/$', views.startexam, name='startexam'),
    # url(r'^home/$', views.home, name='home'),
    # url(r'^show/$', views.show, name='show'),
    # url(r'^result/$', views.result, name='result'),
    # url(r'^login/$', auth_views.login, {'template_name': 'exam/registration/login.html'},  name ='login'),
    # url(r'^logout/$', views.logout, name='logout'),
    # url(r'^myregistration/$', views.myregistration, name='myregistration'),
    # url(r'^testform/$', views.testform, name='testform'),
    # url(r'^fileupload/$', views.fileupload, name= 'fileupload'),
    # url(r'^ajax/text/$', views.ajax, name='ajax'),
    # url(r'^auth/django/', include('django.contrib.auth.urls')),
    # url(r'^auth/login', auth_views.login, {'template_name': 'exam/auth/login.html'}, name='authlogin'),
    
    
    
   
    
    
   
]