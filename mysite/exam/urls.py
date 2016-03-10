from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls
from django.conf.urls import include, url

from . import views
app_name = 'exam'

urlpatterns = [

    # ex: /polls/
    #url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_set_id>[0-9]+)/startexam/$', views.startexam, name='startexam'),
    url(r'^home/$', views.home, name='home'),
    url(r'^show/$', views.show, name='show'),
    url(r'^result/$', views.result, name='result'),
    # url(r'^login/$', auth_views.login, {'template_name': 'exam/registration/login.html'},  name ='login'),
    # url(r'^register/$', views.register_user,  name ='register'),    
    # url(r'^logout/$', views.logout, name='logout'),

    # url(r'^registration/$', views.register, name='registration'),
    url(r'^testform/$', views.testform, name='testform'),
    url(r'^fileupload/$', views.fileupload, name= 'fileupload'),
    url(r'^ajax/text/$', views.ajax, name='ajax'),
  
    
    
    
   
    
    
   
]