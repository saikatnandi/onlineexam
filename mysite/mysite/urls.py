"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views
# from qa1.views import register as qa1_register
from qa1 import views as qa1_views
from readingmaterial import views as readingmaterial_views
from dashboard import views as dashboard_views


from ckeditor_uploader import views as ckeditor_views
from django.views.decorators.cache import never_cache


urlpatterns = [
    url(r'^polls/', include('polls.urls',  namespace="polls")),
    url(r'^qa1/', include('qa1.urls', namespace="qa1")),
    # url(r'^mcq/', include('mcq.urls')),
    url(r'^exam/', include('exam.urls')),
    url(r'^question/', include ('question.urls')),
    url(r'^blog/',include('blog.urls')),
    url(r'^readingmaterial/', include ('readingmaterial.urls') ),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', include ('dashboard.urls')),
    url(r'^feedback/', include ('feedback.urls')),

    # url(r'^select2/', include('django_select2.urls')),
    # url(r'^dashboard/$', readingmaterial_views.dashboard, name= 'dashboard'),

    # url(r'^excelparsing/$', qa1.views.excelparsing, name= 'excelparsing'),



    # url(r'^login/$', auth_views.login, {'template_name': 'readingmaterial/registration/login.html'},  name ='login'),

    url(r'^login/$', qa1_views.mylogin,  name ='login'),

  
    url(r'^logout/$', qa1_views.mylogout, name='logout'),
    url(r'^registration/$', qa1_views.register, name='registration'),  



    url(r'^$', readingmaterial_views.index, name= 'homepage'),
    url(r'^google6bac80d6112145d3.html/$', readingmaterial_views.varification, name= 'varification'),


    url(r'^links/', include('links.urls',  namespace="links")),
    url(r'^notice/', include('notice.urls',  namespace="notice")),
    url(r'^subscription/', include('subscription.urls',  namespace="subscription")),



    # url(r'^comments/', include('django_comments.urls')),
    # url(r'^ckeditor/upload/$', dashboard_views.my_ckeditor_upload, name="ckeditor_upload"),  

    url(r'^ckeditor/upload/', ckeditor_views.upload, name='ckeditor_upload'),
    url(r'^ckeditor/browse/', never_cache(ckeditor_views.browse), name='ckeditor_browse'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
    url('', include('social.apps.django_app.urls', namespace='social'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

SOCIAL_AUTH_URL_NAMESPACE = 'social'