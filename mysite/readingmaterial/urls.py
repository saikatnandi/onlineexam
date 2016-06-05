from django.conf.urls import url

from . import views

app_name = 'readingmaterial'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', views.subtopic1, name='subtopic1'),
    url(r'^topic/(?P<topic_id>[0-9]+)/mcq/(?P<choice>[0-9]+)/$', views.subtopic1_mcq, name='subtopic1_mcq'),
    # url(r'^topic/(?P<topic_id>[0-9]+)/mcq_sub/$', views.subtopic1_mcq_sub, name='subtopic1_mcq_sub'),
    # url(r'^topic/(?P<topic_id>[0-9]+)/mcq_other/$', views.subtopic1_mcq_other, name='subtopic1_mcq_other'),


    url(r'^subtopic/(?P<subtopic1_id>[0-9]+)/$', views.reading_content_list, 
        name='readingcontentlist'),

    url(r'^subtopic/(?P<subtopic1_id>[0-9]+)/mcq/(?P<choice>[0-9]+)/$', views.reading_content_list_mcq, 
        name='readingcontentlist_mcq'),



    # url(r'^topic/(?P<topic_id>[0-9]+)/subtopic/(?P<subtopic1_id>[0-9]+)/content/(?P<reading_content_id>[0-9]+)/$', views.reading_content_details, name='subtopic2'),
    url(r'^content/(?P<reading_content_id>[0-9]+)/finished/$', views.reading_content_finished, name='content_finished'),
    url(r'^content/(?P<reading_content_id>[0-9]+)/unfinished/$', views.reading_content_unfinished, name='content_unfinished'),
    url(r'^content/(?P<reading_content_id>[0-9]+)/$', views.reading_content_details, name='content'),
    url(r'^content/(?P<reading_content_id>[0-9]+)/mcq/$', views.reading_content_details_mcq,
             name='content_mcq'),


    url(r'^question/(?P<quick_question_id>[0-9]+)/$', views.quick_question_details, name='quick_question'),
    url(r'^mcq/(?P<mcq_question_id>[0-9]+)/$', views.mcq_question_details, name='mcq_question'),
    

    url(r'^ajax/addnote/$', views.ajax_addnote, name='ajax_addnote'),
    url(r'^ajax/deletenote/$', views.ajax_deletenote, name='ajax_deletenote'),
    
    url(r'^ajax/addcomment/$', views.ajax_addcomment, name='ajax_comment'),
    url(r'^ajax/deletecomment/$', views.ajax_deletecomment, name='ajax_deletecomment'),
    



    url(r'^ajax/addmcq/$', views.ajax_addmcq, name='ajax_addmcq'),
    url(r'^ajax/deletemcq/$', views.ajax_deletemcq, name='ajax_deletemcq'),
    url(r'^ajax/reportmcq/$', views.ajax_reportmcq, name='ajax_reportmcq'),


    url(r'^ajax/addquestion/$', views.ajax_addquestion, name='ajax_addquestion'),
    url(r'^ajax/deletequestion/$', views.ajax_deletequestion, name='ajax_deletequestion'),

   
    url(r'^ajax/addmarkedtext/$', views.ajax_add_marked_text, name='ajax_add_marked_text'),
    url(r'^ajax/deletemarkedtext/$', views.ajax_delete_marked_text, name='ajax_delete_marked_text'),


    # url(r'^dashboard/$', views.dashboard, name= 'dashboard'),
    

   
]

    # url(r'^allposts/(?P<post_id>[0-9]+)/$', views.post_details, name='post_details'),