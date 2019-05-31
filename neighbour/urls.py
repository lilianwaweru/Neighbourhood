from django.conf.urls import url
from . import views

urlpatterns=[
   url('^$',views.index,name = 'index'),
   url(r'posts/$',views.welcome,name = 'welcome'),
   url(r'^profile/$',views.profile, name = 'ProfileForm'),
]   