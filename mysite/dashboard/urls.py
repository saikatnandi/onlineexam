from django.conf.urls import url

from . import views
app_name = 'dashboard'
urlpatterns = [
    # # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^notes/$', views.notes, name='notes'),
    url(r'^notes/topic/(?P<topic_id>[0-9]+)/$', views.notes_topic, name='notes_topic'),


    url(r'^mcq/$', views.mcq_question, name='mcq_question'),
    url(r'^mcq/topic/(?P<topic_id>[0-9]+)/$', views.mcq_question_topic, name='mcq_question_topic'),


    url(r'^quick/$', views.quick_question, name='quick_question'),
    url(r'^quick/topic/(?P<topic_id>[0-9]+)/$', views.quick_question_topic, name='quick_question_topic'),

    url(r'^notification/$', views.notification, name='notification'),
    url(r'^message/$', views.message, name='message'),
    url(r'^finished_content/$', views.finished_content, name='finished_content'),
    url(r'^mysubscription/$', views.mysubscription, name='mysubscription'),

    url(r'^myresult/$', views.myresult, name='myresult'),







    # url(r'^(?P<notice_id>[0-9]+)/$', views.notice_details, name='notice_details'),
    # url(r'^topic/(?P<topic_id>[0-9]+)/$', views.topic_details, name='topic_details'),
    # # url(r'^topic/(?P<topic_id>[0-9]+)/notice/(?P<notice_id>[0-9]+)$', views.notice_details2, name='notice_details2'),
    



   
]