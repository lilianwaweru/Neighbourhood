from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static   

urlpatterns=[
   url('^$',views.index,name = 'index'),
   url(r'^posts/$',views.welcome,name = 'welcome'),
   url(r'^profile/$',views.profile, name = 'profile'),
   url(r'^viewprofile/$',views.view_profile,name ='view_profile'),
   url(r'^view_business/$',views.view_business,name = 'view_business'),
   url(r'^business/$',views.business,name = 'business'),
   url(r'^create_post/$',views.create_post,name = 'create_post'),
   url(r'^view_post/$',views.view_post,name = 'view_post')
]   

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)