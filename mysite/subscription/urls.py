from django.conf.urls import url

from . import views
app_name = 'subscription'
urlpatterns = [
    # # ex: /polls/
    url(r'^$', views.index, name='index'),

    url(r'^plan/(?P<plan_id>[0-9]+)/$', views.subscribe, name='subscribe'),




    # url(r'^(?P<notice_id>[0-9]+)/$', views.notice_details, name='notice_details'),
    # url(r'^topic/(?P<topic_id>[0-9]+)/$', views.topic_details, name='topic_details'),
    # # url(r'^topic/(?P<topic_id>[0-9]+)/notice/(?P<notice_id>[0-9]+)$', views.notice_details2, name='notice_details2'),
    
  
]