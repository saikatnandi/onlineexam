from django.conf.urls import url

from . import views
app_name = 'readingmaterial'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', views.subtopic1, name='subtopic1'),
    url(r'^topic/(?P<topic_id>[0-9]+)/subtopic/(?P<subtopic1_id>[0-9]+)/$', views.reading_content_list, name='readingcontentlist'),
    url(r'^topic/(?P<topic_id>[0-9]+)/subtopic/(?P<subtopic1_id>[0-9]+)/content/(?P<reading_content_id>[0-9]+)/$', views.reading_content_details, name='subtopic2'),
    url(r'^ajax/addnote/$', views.ajax_addnote, name='ajax_addnote'),
    url(r'^ajax/deletenote/$', views.ajax_deletenote, name='ajax_deletenote'),
    
    url(r'^ajax/addcomment/$', views.ajax_addcomment, name='ajax_comment'),
    url(r'^ajax/addmcq/$', views.ajax_addmcq, name='ajax_addmcq'),
    url(r'^ajax/deletemcq/$', views.ajax_deletemcq, name='ajax_deletemcq'),
   
    url(r'^ajax/addmarkedtext/$', views.ajax_add_marked_text, name='ajax_add_marked_text'),
    url(r'^ajax/deletemarkedtext/$', views.ajax_delete_marked_text, name='ajax_delete_marked_text'),


    # url(r'^dashboard/$', views.dashboard, name= 'dashboard'),
    

   
]

    # url(r'^allposts/(?P<post_id>[0-9]+)/$', views.post_details, name='post_details'),