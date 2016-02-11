from django.conf.urls import url

from . import views
app_name = 'exam'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^show/$', views.show, name='show'),
    url(r'^result/$', views.result, name='result'),
    
   
]