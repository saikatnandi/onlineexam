from django.conf.urls import url

from . import views
app_name = 'feedback'
urlpatterns = [
    # # ex: /polls/
    # url(r'^$', views.index, name='index'),
    url(r'^ajax/addmessage/$', views.ajax_addmessage, name='ajax_addmessage'),
    # url(r'^mcq/$', views.mcq_question, name='mcq_question'),
    # url(r'^quick/$', views.quick_question, name='quick_question'),
    # url(r'^notification/$', views.notification, name='notification'),
    # url(r'^message/$', views.message, name='message'),





   
]