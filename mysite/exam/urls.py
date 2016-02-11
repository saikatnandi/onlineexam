from django.conf.urls import url

from . import views
app_name = 'exam'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_set_id>[0-9]+)/startexam/$', views.startexam, name='startexam'),
    url(r'^home/$', views.home, name='home'),
    url(r'^show/$', views.show, name='show'),
    url(r'^result/$', views.result, name='result'),
    
   
]