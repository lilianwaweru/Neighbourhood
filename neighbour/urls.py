from django.conf.urls import url
from . import views

urlpatterns=[
   url('^$',views.index,name = 'index'),
   url(r'posts/$',views.welcome,name = 'welcome'),
   url(r'^profile/$',views.profile, name = 'Profile'),
   url(r'^viewprofile/$',views.view_profile,name ='view_profile'),
   
]   