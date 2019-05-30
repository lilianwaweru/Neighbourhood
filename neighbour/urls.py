from django.conf.urls import url
from . import views

urlpatterns=[
   url(r'posts/$',views.welcome,name = 'welcome'),